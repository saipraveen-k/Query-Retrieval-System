import openai
import json
from app.core.config import settings

# Initialize OpenAI client
client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

async def call_gpt4(question, chunks):
    """Call OpenAI API for chat completion."""
    context = "\n".join(chunks)
    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that analyzes policy documents and provides structured JSON responses."
        },
        {
            "role": "user",
            "content": (
                f"Given the following policy document clauses:\n{context}\n\n"
                f"Answer the question: {question}\n"
                "Respond in structured JSON: {\"decision\": \"yes/no/partially\", \"justification\": \"<why>\", \"source_clauses\": [\"<chunk_text>\"]}"
            )
        }
    ]
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.2,
            max_tokens=2048
        )
        
        # Extract the response content
        result = response.choices[0].message.content
        
        # Ensure it's valid JSON, fallback if needed
        try:
            json.loads(result)
            return result
        except json.JSONDecodeError:
            # If response isn't valid JSON, wrap it
            return json.dumps({
                "decision": "error",
                "justification": f"Invalid JSON response: {result}",
                "source_clauses": []
            })
            
    except Exception as e:
        return json.dumps({
            "decision": "error",
            "justification": f"API Error: {str(e)}",
            "source_clauses": []
        })
