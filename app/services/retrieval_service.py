import logging

async def retrieve_topk_chunks(query_embedding: list, pinecone_index, top_k: int = 5):
    """
    Retrieve top-k most relevant chunks from Pinecone based on query embedding.
    
    Args:
        query_embedding: The embedding vector for the query
        pinecone_index: Pinecone index instance
        top_k: Number of top chunks to retrieve
    
    Returns:
        List of chunk IDs that are most relevant to the query
    """
    try:
        # Query Pinecone with the embedding
        results = pinecone_index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )
        
        # Extract chunk IDs from results
        chunk_ids = [match.id for match in results.matches]
        return chunk_ids
        
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Error retrieving chunks: {str(e)}")
        return []

def retrieve_context(question: str, file_id: str):
    # existing Pinecone query code...
    chunks = pinecone_query(question, file_id)  # pseudocode — replace with your function
    if not chunks:
        # No relevant text found, skip LLM
        return {
            "decision": "not sure",
            "justification": "No relevant clause found in the provided context.",
            "source_clauses": []
        }
    # join chunk texts into one context string
    context_str = "\n".join(c['text'] for c in chunks)
    return run_llm(question, context_str)
