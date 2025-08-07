from pydantic import BaseModel
from typing import List

class HackRXRunRequest(BaseModel):
    questions: List[str]
    file_path: str

class ClauseReference(BaseModel):
    chunk_text: str

class HackRXRunResponse(BaseModel):
    decision: str
    justification: str
    source_clauses: List[ClauseReference]
