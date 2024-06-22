from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ..meta import Creator
from ..utils import TokenUsage


class TextEncodingResponse(BaseModel):
    id: str = Field(..., alias="_id")
    created_at: datetime
    created_by: Creator
    model: str
    usage: Optional[TokenUsage] = None
    vectors: list[list[float]]


class RawTextEncoding(BaseModel):
    snippets: list[str]
    model: str

    class Config:
        examples = {
            "Minimal": {
                "value": {
                    "model": "sentence-transformers/all-MiniLM-L6-v2",
                    "snippets": [
                        "I like to eat apples.",
                    ],
                },
            },
        }
