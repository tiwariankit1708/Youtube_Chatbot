"""
YouTube Chatbot — Streamlit Web Application
Ask questions about any YouTube video using AI-powered transcript analysis.
"""

import streamlit as st
from dotenv import load_dotenv
from utils.transcript import extract_video_id, get_transcript
from utils.embeddings import create_vector_store
from utils.chain import build_chain

# Load environment variables from .env
load_dotenv()

# ──────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="YouTube Chatbot — Ask Any Video",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ──────────────────────────────────────────────
# Custom CSS — Premium Dark Theme
# ──────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Global ── */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ── Header ── */
    .hero-header {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        margin-bottom: 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(48, 43, 99, 0.4);
    }
    .hero-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.03) 0%, transparent 70%);
        animation: shimmer 8s ease-in-out infinite;
    }
    @keyframes shimmer {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        50% { transform: translate(30px, -20px) rotate(5deg); }
    }
    .hero-header h1 {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #a78bfa, #818cf8, #6366f1, #818cf8, #a78bfa);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-text 4s linear infinite;
        margin-bottom: 0.3rem;
        position: relative;
        z-index: 1;
    }
    @keyframes gradient-text {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    .hero-header p {
        color: #a5b4fc;
        font-size: 1.05rem;
        font-weight: 400;
        letter-spacing: 0.02em;
        position: relative;
        z-index: 1;
    }

    /* ── Status Cards ── */
    .status-card {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.6), rgba(49, 46, 129, 0.4));
        backdrop-filter: blur(12px);
        border: 1px solid rgba(129, 140, 248, 0.2);
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
    }
    .status-card:hover {
        border-color: rgba(129, 140, 248, 0.5);
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.15);
        transform: translateY(-2px);
    }
    .status-card .status-icon {
        font-size: 1.4rem;
        margin-right: 0.5rem;
    }
    .status-card .status-text {
        color: #c7d2fe;
        font-weight: 500;
        font-size: 0.95rem;
    }
    .status-card .status-detail {
        color: #818cf8;
        font-size: 0.82rem;
        margin-top: 0.3rem;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0c29 0%, #1e1b4b 100%);
    }
    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #a5b4fc;
    }
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown li {
        color: #c7d2fe;
    }

    /* ── Chat Bubbles ── */
    .stChatMessage[data-testid="stChatMessage"] {
        border-radius: 16px;
        margin-bottom: 0.6rem;
        animation: fadeIn 0.4s ease-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ── Info / Success boxes ── */
    .info-box {
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.3), rgba(49, 46, 129, 0.2));
        border-left: 4px solid #6366f1;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
        color: #c7d2fe;
    }
    .success-box {
        background: linear-gradient(135deg, rgba(6, 78, 59, 0.3), rgba(4, 120, 87, 0.2));
        border-left: 4px solid #10b981;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
        color: #a7f3d0;
    }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# Hero Header
# ──────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <h1>🎬 YouTube Chatbot</h1>
    <p>Paste a YouTube link and chat with the video — powered by HuggingFace Llama 3 AI</p>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# Session State Initialization
# ──────────────────────────────────────────────
if "chain" not in st.session_state:
    st.session_state.chain = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "video_id" not in st.session_state:
    st.session_state.video_id = None
if "transcript_loaded" not in st.session_state:
    st.session_state.transcript_loaded = False

# ──────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔧 Configuration")
    st.markdown("---")

    youtube_url = st.text_input(
        "🔗 YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste any YouTube video URL that has captions/subtitles enabled."
    )

    process_button = st.button("🚀 Load & Process Video", use_container_width=True, type="primary")

    st.markdown("---")
    st.markdown("## 💡 How It Works")
    st.markdown("""
    1. **Paste** a YouTube video URL
    2. **Click** "Load & Process Video"
    3. **Ask** any question about the video
    4. **Get** AI-powered answers from the transcript
    """)

    st.markdown("---")
    st.markdown("## 🎯 Example Questions")
    st.markdown("""
    - *"What are the main topics discussed?"*
    - *"Summarize the key points"*
    - *"What did the speaker say about...?"*
    - *"Explain the concept of..."*
    """)

    if st.session_state.transcript_loaded:
        st.markdown("---")
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        if st.button("🔄 Load New Video", use_container_width=True):
            st.session_state.chain = None
            st.session_state.messages = []
            st.session_state.video_id = None
            st.session_state.transcript_loaded = False
            st.rerun()

# ──────────────────────────────────────────────
# Video Processing
# ──────────────────────────────────────────────
if process_button and youtube_url:
    video_id = extract_video_id(youtube_url)

    if not video_id:
        st.error("❌ Invalid YouTube URL. Please check the link and try again.")
    else:
        st.session_state.video_id = video_id
        st.session_state.messages = []

        # Show the embedded video
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.video(f"https://www.youtube.com/watch?v={video_id}")

        # Process the transcript
        with st.spinner("📥 Fetching transcript from YouTube..."):
            try:
                transcript = get_transcript(youtube_url)
            except Exception as e:
                st.error(f"❌ Could not fetch transcript: {str(e)}")
                st.info("💡 Make sure the video has captions/subtitles enabled.")
                st.stop()

        st.markdown(f"""
        <div class="status-card">
            <span class="status-icon">📜</span>
            <span class="status-text">Transcript fetched successfully</span>
            <div class="status-detail">{len(transcript):,} characters · ~{len(transcript.split()):,} words</div>
        </div>
        """, unsafe_allow_html=True)

        with st.spinner("🧠 Generating embeddings & building vector store..."):
            try:
                retriever = create_vector_store(transcript)
            except Exception as e:
                st.error(f"❌ Error creating vector store: {str(e)}")
                st.stop()

        with st.spinner("⛓️ Assembling the RAG chain..."):
            chain = build_chain(retriever)
            st.session_state.chain = chain
            st.session_state.transcript_loaded = True

        st.markdown("""
        <div class="success-box">
            ✅ <strong>Ready to chat!</strong> Ask any question about the video below.
        </div>
        """, unsafe_allow_html=True)

        st.rerun()

# ──────────────────────────────────────────────
# Video Preview (when loaded)
# ──────────────────────────────────────────────
if st.session_state.transcript_loaded and st.session_state.video_id:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.video(f"https://www.youtube.com/watch?v={st.session_state.video_id}")

# ──────────────────────────────────────────────
# Chat Interface
# ──────────────────────────────────────────────
if st.session_state.transcript_loaded:
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="🧑‍💻" if message["role"] == "user" else "🤖"):
            st.markdown(message["content"])

    # Chat input
    if user_question := st.chat_input("Ask a question about the video..."):
        # Show user message
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(user_question)

        # Generate answer
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                try:
                    answer = st.session_state.chain.invoke(user_question)
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    error_msg = f"❌ Error generating answer: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
else:
    # Landing state — no video loaded yet
    st.markdown("""
    <div class="info-box">
        👈 <strong>Get started</strong> by pasting a YouTube URL in the sidebar and clicking "Load & Process Video".
    </div>
    """, unsafe_allow_html=True)

    # Feature cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="status-card">
            <span class="status-icon">🎥</span>
            <span class="status-text">Any YouTube Video</span>
            <div class="status-detail">Works with any video that has captions enabled</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="status-card">
            <span class="status-icon">🧠</span>
            <span class="status-text">Llama 3 AI Powered</span>
            <div class="status-detail">Uses Meta's Llama 3 via HuggingFace for accurate answers</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="status-card">
            <span class="status-icon">💬</span>
            <span class="status-text">Natural Conversation</span>
            <div class="status-detail">Ask follow-up questions naturally</div>
        </div>
        """, unsafe_allow_html=True)
