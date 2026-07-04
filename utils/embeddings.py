"""
Embedding and vector store utilities.
Splits transcript text into chunks, generates HuggingFace embeddings,
and stores them in a FAISS vector store for similarity retrieval.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_store(transcript_text: str, chunk_size: int = 1000, chunk_overlap: int = 200):
    """
    Split transcript text into chunks, embed them with HuggingFace BGE, and store in FAISS.

    Args:
        transcript_text: The full transcript as a single string.
        chunk_size: Maximum number of characters per chunk (default 1000).
        chunk_overlap: Number of overlapping characters between chunks (default 200).

    Returns:
        A LangChain retriever configured for similarity search (top-k=4).
    """
    # Split the transcript into manageable chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.create_documents([transcript_text])

    # Generate embeddings using HuggingFace BGE model and build FAISS vector store
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en-v1.5"
    )
    vector_store = FAISS.from_documents(chunks, embeddings)

    # Return a retriever for similarity search
    retriever = vector_store.as_retriever(
        search_type='similarity',
        search_kwargs={"k": 4}
    )
    return retriever
