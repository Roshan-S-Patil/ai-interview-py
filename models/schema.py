from pydantic import BaseModel
from typing import List, Optional, Any

class ChatRequest(BaseModel):
    thread_id: str
    messages: List[dict]  # each dict with keys like {"role": "human"/"ai", "content": str}

class ChatResponse(BaseModel):
    messages: List[dict]  # full conversation messages back
