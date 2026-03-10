import json
from openai import OpenAI
from app.core.config import settings  # make sure you import your settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def call_gpt4(question: str, chunk_texts: list[str]):
    """
    Call GPT-4 with a question and relevant chunk texts.
    
    Args:
        question: The user's question
        chunk_texts: List of relevant text chunks
    
    Returns:
        GPT-4 response
    """
    try:
        # Join chunk texts into context
        context = "\n".join(chunk_texts)
        
        prompt = f"""
You are an expert insurance policy analyst. 
You will be given a question and some excerpts from an insurance policy document. 
Please provide a clear and concise answer based only on the provided context.

Question: {question}

Context:
{context}

Answer:
"""
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful insurance policy analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        return f"Error generating response: {str(e)}"

def run_llm(question: str, retrieved_context: str):
    # Strict JSON-format prompt
    prompt = f"""
You are an expert insurance policy analyst. 
You will be given a question and some excerpts (context) from an insurance policy document. 
Your job is to answer strictly in the following JSON format:

{{
  "decision": "yes" | "no" | "not sure",
  "justification": "<short reason based only on the provided context>",
  "source_clauses": ["<exact excerpt 1>", "<exact excerpt 2>", ...]
}}

If the answer cannot be determined from the provided context, respond only with:

{{
  "decision": "not sure",
  "justification": "No relevant clause found in the provided context.",
  "source_clauses": []
}}

Do NOT ask for more information. Do NOT output anything except valid JSON.
---
Question: {question}
Context:
{retrieved_context}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # or your preferred OpenAI model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that only outputs valid JSON as instructed."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            response_format={"type": "json_object"}  # forces JSON mode if supported
        )

        content = response.choices[0].message.content.strip()
        
        # Parse JSON safely
        try:
            result = json.loads(content)
        except json.JSONDecodeError:
            result = {
                "decision": "error",
                "justification": "Model did not return valid JSON.",
                "source_clauses": []
            }
        return result

    except Exception as e:
        return {
            "decision": "error",
            "justification": f"LLM API Error: {str(e)}",
            "source_clauses": []
        }
