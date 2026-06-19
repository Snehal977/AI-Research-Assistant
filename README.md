# AI Research Assistant

An AI-powered Research Assistant that allows users to upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG). The system extracts text from PDFs, processes it into chunks, stores them in a vector database, retrieves the most relevant information, and generates context-aware answers using Google's Gemini model.

---

## Features

* Upload PDF documents
* Extract and clean PDF text
* Intelligent text chunking
* Vector storage using ChromaDB
* Semantic similarity search
* Retrieval-Augmented Generation (RAG)
* Question Answering using Gemini
* Interactive Streamlit interface
* Display retrieved chunks for transparency

---

## Project Architecture

```text
User Uploads PDF
        ↓
PDF Text Extraction
        ↓
Text Cleaning
        ↓
Chunking
        ↓
ChromaDB Vector Storage
        ↓
Similarity Search
        ↓
Retriever
        ↓
Prompt Construction
        ↓
Gemini LLM
        ↓
Generated Answer
```

---

## Tech Stack

### Programming Language

* Python

### Frontend

* Streamlit

### LLM

* Gemini 2.5 Flash

### Vector Database

* ChromaDB

### PDF Processing

* PyMuPDF (fitz)

### Embeddings

* ChromaDB Embedding Functions

### Environment Management

* Python Virtual Environment (venv)

### Version Control

* Git
* GitHub

---

## Project Structure

```text
AI-Research-Assistant/

├── app.py
├── ingest.py
├── requirements.txt
├── .gitignore

├── dashboards/
│   ├── analytics.py
│   └── charts.py

├── utils/
│   ├── __init__.py
│   ├── chroma_store.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── llm.py
│   ├── pdf_loader.py
│   ├── pdf_processor.py
│   ├── query.py
│   ├── query_rag.py
│   ├── query_test.py
│   ├── rag.py
│   └── retriever.py

├── data/
├── vector_db/
└── screenshots/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Snehal977/AI-Research-Assistant.git

cd AI-Research-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Get your Gemini API key from Google AI Studio.

---

## Run Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## How It Works

### 1. PDF Upload

Users upload a PDF document through the Streamlit interface.

### 2. Text Extraction

Text is extracted from PDF pages using PyMuPDF.

### 3. Text Cleaning

Unwanted spaces and formatting issues are removed.

### 4. Chunking

Large documents are split into smaller chunks for efficient retrieval.

### 5. Vector Storage

Chunks are stored inside ChromaDB.

### 6. Retrieval

Relevant chunks are retrieved using semantic similarity search.

### 7. Prompt Construction

Retrieved chunks and user question are combined into a prompt.

### 8. Answer Generation

Gemini generates an answer based only on the retrieved context.

---

## Example Questions

* What is Machine Learning?
* Explain supervised learning.
* What are the admission eligibility criteria?
* Summarize Chapter 1.
* What are the key concepts discussed in the document?

---

## Future Improvements

* Conversation Memory
* Multi-PDF Support
* Source Citations
* Local LLM Support (Ollama + Mistral)
* LangChain Integration
* Advanced Analytics Dashboard
* User Authentication
* Cloud Deployment

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Vector Databases
* Semantic Search
* ChromaDB
* Streamlit
* PDF Processing
* Git & GitHub
* AI Application Development

---

## Author

Snehal Madhusoodhanan E

B.Tech Information Technology

Aspiring AI/ML Engineer | Python Developer | LLM Enthusiast
