import pinecone
from app.core.config import settings

def setup_pinecone():
    pinecone.init(
        api_key=settings.PINECONE_API_KEY,
        environment=settings.PINECONE_ENV
    )
    if settings.PINECONE_INDEX not in pinecone.list_indexes():
        pinecone.create_index(
            name=settings.PINECONE_INDEX,
            dimension=1536,
            metric='cosine'
        )
    return pinecone.Index(settings.PINECONE_INDEX)
