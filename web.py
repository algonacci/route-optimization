from pydantic import BaseModel, Field
from typing import Dict, Any


class Info(BaseModel):
    status: bool = Field(default=True, description="Response success or failed")
    meta: Dict[str, Any] = Field(default=None, description="Response metadata")
    message: str


class WebResponse(BaseModel):
    info: Info
    data: Any = Field(default=None, description="Response data")
