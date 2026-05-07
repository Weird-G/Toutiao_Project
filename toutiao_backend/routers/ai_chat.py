import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/api/ai", tags=["AI问答"])

DASHSCOPE_API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")
DASHSCOPE_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"


class ChatRequest(BaseModel):
    messages: list


@router.post("/chat")
async def ai_chat(request: ChatRequest):
    if not DASHSCOPE_API_KEY:
        raise HTTPException(status_code=500, detail="DASHSCOPE_API_KEY 未配置")

    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json",
        "X-DashScope-SSE": "enable"
    }
    payload = {
        "model": "qwen3-max-preview",
        "messages": request.messages,
        "stream": True
    }

    async def stream_response():
        async with httpx.AsyncClient(timeout=60.0) as client:
            async with client.stream("POST", DASHSCOPE_ENDPOINT, headers=headers, json=payload) as response:
                response.raise_for_status()
                async for chunk in response.aiter_text():
                    yield chunk

    return StreamingResponse(
        stream_response(),
        media_type="text/event-stream"
    )