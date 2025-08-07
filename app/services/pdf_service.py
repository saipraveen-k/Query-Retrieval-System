import fitz  # PyMuPDF

def parse_pdf_to_chunks(pdf_path: str, chunk_size: int = 450) -> list:
    doc = fitz.open(pdf_path)
    full_text = ''
    for page in doc:
        full_text += page.get_text()
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]
    return chunks
