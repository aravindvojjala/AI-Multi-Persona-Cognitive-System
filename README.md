# 🤖 Grid07 AI – Multi-Persona Cognitive System

An AI-powered system that intelligently routes user input to different AI personas and generates context-aware responses using FastAPI, LangGraph, ChromaDB, and Streamlit.

## 🚀 Features
* 🧠 Multi-Persona AI Routing
  * Automatically selects the most relevant AI bot based on input similarity
* ⚡ FastAPI Backend
  * High-performance API for processing requests
* 🔍 Semantic Search (ChromaDB)
  * Uses embeddings to match user input with personas
* 🔗 LangGraph Workflow
  * Structured AI pipeline (Decide → Search → Generate)
* 🎨 Streamlit Frontend
  * Clean UI to interact with the system
* 🤖 LLM Integration (Cerebras API)
  * Uses LLaMA 3.1 model for response generation

## 🏗️ Project Structure
```
AI_Cognitive_System/
│
├── backend/
│   ├── main.py          # FastAPI app
│   ├── router.py        # Routing logic (semantic matching)
│   ├── graph.py         # LangGraph pipeline
│   ├── personas.py      # AI personas
│   └── db.py            # ChromaDB setup
│
├── frontend/
│   └── app.py           # Streamlit UI
│
├── .env                 # API keys
├── requirements.txt
└── README.md
```

## ⚙️ Installation
### 1️⃣ Clone the Repository
```
git clone <your-repo-url>
cd AI_Cognitive_System
```

### 2️⃣ Create Virtual Environment
```
conda create -n py313env python=3.11
conda activate py313env
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 🔑 Environment Variables

Create a .env file:
```
CEREBRAS_API_KEY=your_api_key_here
```

### ▶️ Running the Project
🔹 Start Backend (FastAPI)
```
uvicorn backend.main:app --reload
```

#### 👉 Runs on:
http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

🔹 Start Frontend (Streamlit)
```
streamlit run frontend/app.py
```

#### 👉 Runs on:
http://localhost:8501

## 🔄 API Usage

##### Endpoint: /generate

##### POST Request
```
{
  "post": "AI is transforming the future"
}
```
##### Response
```
{
  "bots": ["bot_A"],
  "responses": ["Generated response..."]
}
```

## 🧠 How It Works
#### 1. Input Processing
* User enters text in Streamlit UI
#### 2. Semantic Routing
* SentenceTransformer converts input → embeddings
* Compared with stored persona embeddings
* Best matching bot is selected
#### 3. LangGraph Execution
Pipeline:
```
Decide Node → Search Node → Generate Node
```
#### 4. Response Generation
* LLM generates output based on persona

## 🛠️ Tech Stack
* Backend: FastAPI
* Frontend: Streamlit
* LLM: Cerebras (LLaMA 3.1)
* Vector DB: ChromaDB
* Embeddings: SentenceTransformers
* Orchestration: LangGraph


## 📈 Future Improvements
* 🔥 Multi-bot responses (Top-K selection)
* 🌐 Deploy on Render / Railway
* 🧠 Memory-based conversations
* 🎯 Better routing (LLM-based instead of similarity)
*💎 Premium UI (chat-style interface)

## 👨‍💻 Author

Aravind