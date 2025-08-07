import openai

async def call_gpt4(question, chunks):
    context = "\n".join(chunks)
    prompt = (
        f"Given the following policy document clauses:\n{context}\n\n"
        f"Answer the question: {question}\n"
        "Respond in structured JSON: {decision: yes/no/partially, justification: <why>, source_clauses: [<chunk_text>]}"
    )
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user", "content": prompt}],
        temperature=0.2
    )
    return resp['choices'][0]['message']['content']
