from enum import Enum
from pydantic import BaseModel, Field
from typing import Literal, List

class ChatCompletionRole(str, Enum):
    user = 'user'
    assistant = 'assistant'

class ChatCompletionMessage(BaseModel):
    role: ChatCompletionRole
    content: str = Field(..., max_length=5000)

class ChatCompletionModel(BaseModel):
    model: Literal["mixtral-7b", "mistral-7b-chat", "zephyr-7b-alpha", "mistral-7b-chat-trt-llm"]
    messages: List[ChatCompletionMessage]
    stream: bool = False

class EmbeddingsModel(BaseModel):
    model: Literal["nomic-embed-v1.5"]
    inputs: List[str]
    dimensions: Literal[64, 128, 256, 512, 768]
    encoding_format: Literal["float", "base64"] = "float"

class PrivacyModel(BaseModel):
    input: str
    compliance: List[str]
    custom: List[str]

class ModerationsModel(BaseModel):
    input: str
    guardrails: List[str]
