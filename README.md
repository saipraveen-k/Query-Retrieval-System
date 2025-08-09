# LLM-Powered Intelligent Query-Retrieval System

This project is a FastAPI-based backend that processes complex natural language queries on large policy documents (e.g., insurance contracts). It extracts relevant clauses using semantic search with embeddings, then uses GPT-4 to generate explainable, structured JSON answers.

---

## Features

- Upload and parse policy PDF files
- Break documents into text chunks
- Generate embeddings using OpenAI `text-embedding-ada-002`
- Store embeddings in Pinecone vector database
- Store chunk metadata in PostgreSQL database
- Retrieve relevant chunks by semantic similarity for queries
- Use GPT-4 to answer questions with referenced document clauses
- Expose a REST API endpoint that acts as a webhook for external integrations

---

## Prerequisites

- Python 3.8+
- PostgreSQL server
- Pinecone account
- OpenAI API key

---

## Installation

1. Clone the repo

git clone <https://github.com/kruthika224/llm_query_retriever>
cd llm_query_retriever


2. Create a `.env` file based on `.env.example` and fill in your API keys and DB URL:

OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=us-west1-gcp
PINECONE_INDEX=llm-embeddings
DATABASE_URL=postgresql+asyncpg://user:password@localhost/hackrx_db


3. Install dependencies

pip install -r requirements.txt


---

## Configure Database

- Make sure your PostgreSQL server is running.
- Create a database (e.g., `hackrx_db`) and user with proper privileges.
- Run migrations or use SQLAlchemy to auto-create tables (for testing).

---

## Running the Server

Start the FastAPI server locally:

uvicorn app.main:app --reload


This will launch on `http://localhost:8000`

---

## Using the Webhook API

The main webhook endpoint is:

POST /api/v1/hackrx/run


### Request Body (JSON):

{
"questions": [
"Does the policy cover knee surgery in Pune?",
"What is the waiting period for cataract surgery?"
],
"file_path": "C:\\Users\\saipr\\Query-Retrieval-System\\data\\BAJAJ.pdf"
}


- `questions`: List of natural language questions to ask
- `file_path`: Path to the PDF policy document on the server

### Sample curl request:

curl -X POST http://localhost:8000/api/v1/hackrx/run
-H "Content-Type: application/json"
-d '{
"questions": ["Does the policy cover knee surgery in Pune?"],
"file_path": "data/sample_policy.pdf"
}'


### Response:

You will receive a structured JSON response with decisions, justifications, and source clauses extracted from the document.

---

## How it works internally

- Parses the PDF into text chunks
- Generates vector embeddings for chunks via OpenAI
- Stores embeddings in Pinecone and metadata in PostgreSQL
- For a query, generates query embedding, retrieves matching chunks
- Constructs a GPT-4 prompt combining query and chunks
- Returns GPT-4's structured JSON answer referencing clauses

---

## Deploying as a Webhook

- The API endpoint can be called by any external system supporting webhooks.
- Deploy your FastAPI app behind a secure HTTPS endpoint.
- Use API keys or tokens for authentication to protect the webhook.
- External services (Zapier, Integromat, custom apps) can POST questions & document paths and get instant answers.

---

## Notes

- Make sure to keep your API keys secure.
- Adjust chunk size or retrieval settings for performance tuning.
- Use async calls for better concurrency and speed.
- Extend with email/docx support or advanced decision logic as needed.

---

## Troubleshooting

- If Pinecone connection fails, verify your keys and environment.
- If OpenAI calls error, check your API quota and keys.
- Database errors usually involve connection string or setup issues.

---

## License & Contributions

Feel free to fork and improve this repo. Pull requests are welcome!

---

Thank you for using this intelligent query system 🚀  
For questions or help, open an issue or contact the saipraveen-k.
