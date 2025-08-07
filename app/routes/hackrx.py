from fastapi import APIRouter, Depends
from app.schemas.hackrx import HackRXRunRequest
from app.core.db import get_db
from app.core.pinecone_utils import setup_pinecone
from app.services.embedding_service import get_embedding
from app.services.retrieval_service import retrieve_topk_chunks
from app.services.gpt_service import call_gpt4
from app.models.chunk import Chunk

router = APIRouter()

@router.post("/api/v1/hackrx/run")
async def hackrx_run(req: HackRXRunRequest, db=Depends(get_db)):
    pinecone_index = setup_pinecone()
    responses = []
    for q in req.questions:
        q_emb = await get_embedding(q)
        match_ids = await retrieve_topk_chunks(q_emb, pinecone_index)
        chunks = [await db.get(Chunk, id) for id in match_ids]
        chunk_texts = [c.chunk_text for c in chunks if c]
        resp = await call_gpt4(q, chunk_texts)
        responses.append(resp)
    return {"results": responses}
