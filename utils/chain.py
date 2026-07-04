"""
LangChain chain utilities.
Assembles the full RAG (Retrieval-Augmented Generation) chain
using a retriever, prompt template, HuggingFace LLM, and output parser.
"""

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


def _format_docs(retrieved_docs):
    """Join retrieved document page contents with double newlines."""
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def build_chain(retriever):
    """
    Build the full RAG chain that retrieves context and generates an answer.

    The chain:
        1. Takes a question string as input
        2. Retrieves relevant transcript chunks via the retriever
        3. Formats them into a context block
        4. Passes context + question into a prompt template
        5. Sends the prompt to HuggingFace LLM (Meta-Llama-3-8B-Instruct)
        6. Parses the output into a plain string

    Args:
        retriever: A LangChain retriever (e.g., from FAISS vector store).

    Returns:
        A LangChain Runnable chain that accepts a question string and returns an answer string.
    """
    # LLM — HuggingFace Inference Endpoint with Meta Llama 3
    llm_endpoint = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        task="conversational",
        max_new_tokens=512,
        do_sample=False
    )
    llm = ChatHuggingFace(llm=llm_endpoint)

    # Prompt template
    prompt = PromptTemplate(
        template="""You are a helpful assistant that answers questions based on YouTube video transcripts.
Answer only from the provided transcript context. If the context is insufficient, say "I don't have enough information from the video to answer that question."

Context from the video transcript:
{context}

Question: {question}

Answer:""",
        input_variables=['context', 'question']
    )

    # Output parser
    parser = StrOutputParser()

    # Parallel chain: retrieves context and passes through the question
    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(_format_docs),
        'question': RunnablePassthrough()
    })

    # Full chain
    main_chain = parallel_chain | prompt | llm | parser

    return main_chain
