<div align="center">

# 🎬 YouTube Chatbot

### 🤖 Ask Anything About Any YouTube Video — Powered by AI

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*Paste a YouTube link, and chat with the video like you're talking to an expert who watched the whole thing.*

---

</div>

## 📌 About

**YouTube Chatbot** is an AI-powered tool that extracts the transcript from any YouTube video and lets you have a natural conversation about its content. Instead of watching a full video, simply paste the URL and ask questions — the bot provides detailed, context-aware answers based on what was said in the video.

Whether it's a 3-hour lecture, a tech tutorial, or a podcast episode — this chatbot has you covered.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎥 **YouTube Transcript Extraction** | Automatically fetches the full transcript from any YouTube video using `youtube-transcript-api` |
| 💬 **Conversational Q&A** | Ask natural language questions and get detailed, accurate answers from the video content |
| 🧠 **AI-Powered Understanding** | Uses Google Gemini / LLM models to understand context, summarize, and explain video content |
| 🔗 **LangChain Integration** | Built with LangChain for robust prompt management, chaining, and retrieval-augmented generation |
| 🖥️ **Streamlit Web Interface** | Clean, interactive web UI — just paste a link and start chatting |
| 📝 **Smart Summarization** | Get concise summaries of long videos in seconds |
| 🔍 **Context-Aware Responses** | The chatbot maintains conversation context for follow-up questions |

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      USER INTERFACE                          │
│                   (Streamlit Web App)                         │
│                                                              │
│   ┌─────────────┐    ┌──────────────────────────────────┐    │
│   │  YouTube URL │───▶│      Transcript Extraction       │    │
│   └─────────────┘    │   (youtube-transcript-api)        │    │
│                      └──────────────┬───────────────────┘    │
│                                     │                        │
│                                     ▼                        │
│                      ┌──────────────────────────────────┐    │
│                      │      Text Chunking & Processing   │    │
│                      │         (LangChain)               │    │
│                      └──────────────┬───────────────────┘    │
│                                     │                        │
│                                     ▼                        │
│                      ┌──────────────────────────────────┐    │
│                      │       Vector Store / Embeddings    │    │
│                      │        (FAISS / ChromaDB)         │    │
│                      └──────────────┬───────────────────┘    │
│                                     │                        │
│                                     ▼                        │
│   ┌─────────────┐    ┌──────────────────────────────────┐    │
│   │  User Query  │───▶│     LLM (Google Gemini / GPT)    │    │
│   └─────────────┘    │     via LangChain QA Chain        │    │
│                      └──────────────┬───────────────────┘    │
│                                     │                        │
│                                     ▼                        │
│                      ┌──────────────────────────────────┐    │
│                      │        Detailed AI Response        │    │
│                      └──────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** installed on your machine
- A **Google Gemini API Key** (or OpenAI API key, depending on the model you choose)
- **pip** package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tiwariankit1708/Youtube_Chatbot.git
   cd Youtube_Chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser** and navigate to `http://localhost:8501`

---

## 📖 Usage

1. **Paste a YouTube URL** into the input field
2. **Wait** for the transcript to be extracted and processed
3. **Ask any question** about the video in the chat input
4. **Get detailed answers** — follow up with more questions as needed!

### 💡 Example Questions You Can Ask

> *"What are the main points discussed in this video?"*
>
> *"Explain the concept mentioned at the beginning of the video."*
>
> *"Summarize this video in 5 bullet points."*
>
> *"What solution did the speaker suggest for the problem?"*
>
> *"Can you explain the technical details discussed around the middle of the video?"*

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web application framework for the UI |
| **LangChain** | LLM orchestration, prompt templates, and QA chains |
| **Google Gemini** | Large Language Model for generating responses |
| **youtube-transcript-api** | Extracting transcripts from YouTube videos |
| **FAISS / ChromaDB** | Vector store for efficient similarity search |
| **dotenv** | Environment variable management |

---

## 📁 Project Structure

```
Youtube_Chatbot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── utils/                  # Utility modules
    ├── transcript.py       # YouTube transcript extraction
    ├── embeddings.py       # Text embedding & vector store
    └── chain.py            # LangChain QA chain setup
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## ⚠️ Limitations

- Only works with YouTube videos that have **transcripts/subtitles** available
- Accuracy depends on the **quality of the transcript** (auto-generated captions may have errors)
- Very long videos may take **longer to process** due to transcript size
- Requires an **active internet connection** and a valid API key

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Ankit Tiwari**

- GitHub: [@tiwariankit1708](https://github.com/tiwariankit1708)

---

<div align="center">

### ⭐ If you found this project useful, give it a star!

*Built with ❤️ and AI*

</div>
