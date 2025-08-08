from pinecone import Pinecone, ServerlessSpec
from app.core.config import settings

def setup_pinecone():
    pc = Pinecone(
        api_key=settings.PINECONE_API_KEY
    )
    if settings.PINECONE_INDEX not in pc.list_indexes().names():
        pc.create_index(
            name=settings.PINECONE_INDEX,
            dimension=1536,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region=settings.PINECONE_ENV
            )
        )
    return pc.Index(settings.PINECONE_INDEX)
