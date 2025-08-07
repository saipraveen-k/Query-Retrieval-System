import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

async def get_embedding(text: str) -> list:
    resp = openai.Embedding.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return resp['data'][0]['embedding']
