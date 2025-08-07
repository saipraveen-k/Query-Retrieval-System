import pinecone
from app.models.chunk import Chunk

async def store_chunk_with_embedding(chunk, embedding, filename, db_session, pinecone_index):
    pinecone_id = f"{filename}_{hash(chunk)}"
    pinecone_index.upsert([(pinecone_id, embedding)])
    db_chunk = Chunk(filename=filename, chunk_text=chunk, embedding_id=pinecone_id)
    db_session.add(db_chunk)
    await db_session.commit()

async def retrieve_topk_chunks(question_embedding, pinecone_index, k=5):
    results = pinecone_index.query(vector=question_embedding, top_k=k, include_metadata=False)
    return [match['id'] for match in results['matches']]
