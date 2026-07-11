<div align="center">

# 🎬 YouTube Chatbot

### 🤖 Ask Anything About Any YouTube Video — Powered by AI

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*Paste a YouTube link, and chat with the video like you're talking to an expert who watched the whole thing.*

> 📅 **Last Updated:** July 2026

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
| 🧠 **AI-Powered Understanding** | Uses Meta Llama 3 via HuggingFace to understand context, summarize, and explain video content |
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
│                      │   (FAISS + HuggingFace BGE)       │    │
│                      └──────────────┬───────────────────┘    │
│                                     │                        │
│                                     ▼                        │
│   ┌─────────────┐    ┌──────────────────────────────────┐    │
│   │  User Query  │───▶│   LLM (Meta Llama 3 / HuggingFace)│    │
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
- A **HuggingFace API Token** — get one free at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- **pip** package manager

### 🔧 First-Time Setup (Full Installation)

Open a terminal in the project folder and run these commands **one by one**:

1. **Clone the repository**
   ```bash
   git clone https://github.com/tiwariankit1708/Youtube_Chatbot.git
   cd Youtube_Chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\activate
   ```
   **Windows (CMD):**
   ```cmd
   venv\Scripts\activate.bat
   ```
   **macOS / Linux:**
   ```bash
   source venv/bin/activate
   ```

   > ✅ You'll see `(venv)` appear at the start of your terminal prompt when activated.

4. **Install all dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API key**

   Open the `.env` file in the project root and replace the placeholder with your actual HuggingFace token:
   ```env
   HF_TOKEN=your_huggingface_api_token_here
   ```
   > 💡 Get your free token at: https://huggingface.co/settings/tokens

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

7. **Open your browser** and go to `http://localhost:8501`

---

### 🔄 Returning to the Project (Next Time)

Already set up? Just run these **2 commands** to get back up and running:

**Windows (PowerShell):**
```powershell
.\venv\Scripts\activate
streamlit run app.py
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
streamlit run app.py
```

**macOS / Linux:**
```bash
source venv/bin/activate
streamlit run app.py
```

> ⚠️ Always activate the virtual environment **before** running the app, otherwise Python won't find the installed libraries.

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
| **HuggingFace (Llama 3)** | Large Language Model for generating responses |
| **HuggingFace Embeddings (BGE)** | BAAI/bge-large-en-v1.5 for document embeddings |
| **youtube-transcript-api** | Extracting transcripts from YouTube videos |
| **FAISS** | Vector store for efficient similarity search |
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
