# LLM-Powered Intelligent Query-Retrieval System

This project is a FastAPI-based backend that processes complex natural language queries on large policy documents (e.g., insurance contracts). It extracts relevant clauses using semantic search with embeddings, then uses GPT-4 to generate explainable, structured JSON answers.

---

## 🚀 Features

- **PDF Processing**: Upload and parse policy PDF files with PyMuPDF
- **Intelligent Chunking**: Break documents into optimal text chunks for retrieval
- **Semantic Search**: Generate embeddings using OpenAI `text-embedding-ada-002`
- **Vector Database**: Store embeddings in Pinecone vector database
- **Metadata Storage**: Store chunk metadata in PostgreSQL database
- **Smart Retrieval**: Retrieve relevant chunks by semantic similarity for queries
- **AI-Powered Answers**: Use GPT-4 to answer questions with referenced document clauses
- **REST API**: Expose REST API endpoints for external integrations
- **Webhook Support**: Built-in webhook endpoint for external system integration

---

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL server
- Pinecone account
- OpenAI API key

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/kruthika224/llm_query_retriever
cd llm_query_retriever
```

### 2. Create environment file
Create a `.env` file in the root directory:
```bash
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=us-west1-gcp
PINECONE_INDEX=llm-embeddings
DATABASE_URL=postgresql+asyncpg://user:password@localhost/hackrx_db
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

1. Ensure PostgreSQL server is running
2. Create database and user:
```sql
CREATE DATABASE hackrx_db;
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE hackrx_db TO your_user;
```

3. Run database migrations:
```bash
alembic upgrade head
```

---

## 🏃‍♂️ Running the Server

### Development mode:
```bash
uvicorn app.main:app --reload
```

### Production mode:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

---

## 📖 API Documentation

### Interactive Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 🔌 API Endpoints

### 1. HackRx Query Endpoint
**POST** `/api/v1/hackrx/run`

#### Request Body:
```json
{
  "questions": [
    "Does the policy cover knee surgery in Pune?",
    "What is the waiting period for cataract surgery?"
  ],
  "file_path": "data/BAJAJ.pdf"
}
```

#### Response:
```json
{
  "results": [
    {
      "question": "Does the policy cover knee surgery in Pune?",
      "answer": "Yes, knee surgery is covered...",
      "confidence": 0.95,
      "source_clauses": [...]
    }
  ]
}
```

### 2. Webhook Endpoint
**POST** `/webhook/process`

#### Request Body:
```json
{
  "event_type": "document_processed",
  "data": {...}
}
```

---

## 🧪 Testing

### Using curl:
```bash
# Test the main endpoint
curl -X POST http://localhost:8000/api/v1/hackrx/run \
  -H "Content-Type: application/json" \
  -d '{
    "questions": ["Does the policy cover knee surgery?"],
    "file_path": "data/BAJAJ.pdf"
  }'
```

### Using the test client:
```bash
python hackrx_test_client.py
```

---

## 🏗️ Project Structure

```
Query-Retrieval-System/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── core/
│   │   ├── config.py          # Configuration management
│   │   ├── db.py              # Database connection
│   │   └── pinecone_utils.py  # Pinecone utilities
│   ├── models/
│   │   └── chunk.py           # SQLAlchemy models
│   ├── routes/
│   │   ├── hackrx.py          # Main API routes
│   │   └── webhook.py         # Webhook routes
│   ├── schemas/
│   │   └── hackrx.py          # Pydantic schemas
│   └── services/
│       ├── embedding_service.py  # Embedding generation
│       ├── retrieval_service.py  # Document retrieval
│       ├── gpt_service.py        # GPT-4 integration
│       └── pdf_service.py        # PDF processing
├── data/                      # Sample PDF documents
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .env.example              # Environment variables template
```

---

## 🔧 Configuration

### Environment Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | `sk-...` |
| `PINECONE_API_KEY` | Pinecone API key | `...` |
| `PINECONE_ENV` | Pinecone environment | `us-west1-gcp` |
| `PINECONE_INDEX` | Pinecone index name | `llm-embeddings` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+asyncpg://...` |

---

## 🔄 How It Works

1. **PDF Upload**: PDF documents are uploaded to the `data/` directory
2. **Processing**: PDFs are parsed into text chunks using PyMuPDF
3. **Embedding**: Each chunk gets vector embeddings via OpenAI
4. **Storage**: Embeddings go to Pinecone, metadata to PostgreSQL
5. **Query**: User questions are embedded and matched against stored chunks
6. **Answer**: GPT-4 generates answers using retrieved context

---

## 🚀 Deployment Options

### Docker (Recommended)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Cloud Platforms
- **Heroku**: Deploy with Procfile
- **AWS**: Use EC2 or ECS
- **Google Cloud**: Use Cloud Run or GKE
- **Azure**: Use Container Instances or AKS

---

## 🔍 Monitoring & Logging

### Health Check Endpoint
**GET** `/health`

### Logging
- Application logs are written to stdout
- Use structured logging with correlation IDs
- Monitor with tools like Datadog or CloudWatch

---

## ⚡ Performance Optimization

### Tips:
- Adjust chunk size based on document complexity
- Use async processing for better concurrency
- Implement caching for frequently accessed documents
- Monitor API rate limits

---

## 🐛 Troubleshooting

### Common Issues:

| Issue | Solution |
|-------|----------|
| **Pinecone connection fails** | Verify API keys and environment settings |
| **OpenAI rate limits** | Check API quota and implement retry logic |
| **Database connection errors** | Verify DATABASE_URL and PostgreSQL setup |
| **PDF parsing issues** | Ensure PDF is not corrupted or password-protected |

### Debug Mode:
```bash
uvicorn app.main:app --reload --log-level debug
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Support

- **Issues**: [GitHub Issues](https://github.com/kruthika224/llm_query_retriever/issues)
- **Discussions**: [GitHub Discussions](https://github.com/kruthika224/llm_query_retriever/discussions)
- **Email**: Contact repository maintainers

---

## 🎉 Acknowledgments

- OpenAI for GPT-4 and embeddings API
- Pinecone for vector database
- FastAPI team for the excellent framework
- Contributors and testers

---

**Happy Querying!** 🚀

*Last updated: December 2024*
