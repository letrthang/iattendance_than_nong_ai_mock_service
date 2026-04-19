import random
import time
import uuid
from datetime import datetime, timezone
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.responses import MOCK_RESPONSES

app = FastAPI(
    title="Thần Nông AI — Mock Service",
    description=(
        "Mock API for iAttendance **Thần Nông AI**.\n\n"
        "Responses are randomly selected from a pool of **100 pre-written messages** "
        "covering iAttendance domains: attendance, leave, payslip, orders, farm, support, and more.\n\n"
        "**Two API groups:**\n"
        "- **OpenClaw-compatible** — `/api/v1/sessions/*` and `/api/v1/gateway/*`\n"
        "- **OpenAI-compatible** — `/v1/chat/completions`\n\n"
        "**Authentication:** All endpoints accept `Authorization: Bearer <token>` header (not validated in mock).\n\n"
        "**Base URL (production mock):** `https://iattendance-than-nong-ai-mock-service.onrender.com`"
    ),
    version="2.0.0",
    contact={"name": "iAttendance Team"},
    license_info={"name": "MIT"},
)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

tags_metadata = [
    {"name": "System", "description": "Health check and service info."},
    {"name": "Gateway (OpenClaw)", "description": "OpenClaw-compatible gateway management endpoints."},
    {"name": "Sessions (OpenClaw)", "description": "OpenClaw-compatible session endpoints: create, list, send messages."},
    {"name": "Chat Completions (OpenAI)", "description": "OpenAI-compatible `/v1/chat/completions` endpoint."},
]
app.openapi_tags = tags_metadata

# ── In-memory store ──────────────────────────────────────────────────────────
_sessions: dict = {}
_gateway_running: bool = True


def _now():
    return datetime.now(timezone.utc).isoformat()


def _session(sid, cid="", uid=""):
    if sid not in _sessions:
        _sessions[sid] = {
            "meta": {"session_id": sid, "company_id": cid, "user_id": uid,
                     "title": "New conversation", "created_at": _now()},
            "messages": []
        }
    return _sessions[sid]


# ── Pydantic models ─────────────────────────────────────────────────────────


# OpenClaw
class OpenClawCreateSessionRequest(BaseModel):
    sessionKey: Optional[str] = Field(None, example="main")
    company_id: Optional[str] = Field("", example="cmp-001")
    user_id: Optional[str] = Field("", example="usr-001")
    title: Optional[str] = Field("New conversation", example="Hỏi về chấm công")


class OpenClawSendRequest(BaseModel):
    sessionKey: str = Field(..., example="main")
    message: str = Field(..., example="Hello from external service!")


# OpenAI
class OpenAIChatMessage(BaseModel):
    role: str = Field(..., example="user")
    content: str = Field(..., example="Hello!")


class OpenAIChatRequest(BaseModel):
    model: str = Field("thannong-ai-mock", example="deepseek/deepseek-chat")
    messages: List[OpenAIChatMessage] = Field(...)
    temperature: Optional[float] = Field(0.7, example=0.7)
    max_tokens: Optional[int] = Field(None, example=100)
    stream: Optional[bool] = Field(False, example=False)
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    stop: Optional[list] = None


# ═════════════════════════════════════════════════════════════════════════════
# SYSTEM
# ═════════════════════════════════════════════════════════════════════════════

@app.get("/health", tags=["System"], summary="Health check")
def health():
    return {"status": "ok", "service": "thannong-ai-mock", "version": "2.0.0", "timestamp": _now()}


# ═════════════════════════════════════════════════════════════════════════════
# OPENCLAW-COMPATIBLE — GATEWAY
# ═════════════════════════════════════════════════════════════════════════════

@app.post("/api/v1/gateway/start", tags=["Gateway (OpenClaw)"], summary="Start the gateway")
def gateway_start(authorization: Optional[str] = Header(None)):
    global _gateway_running
    _gateway_running = True
    return {"status": "started", "timestamp": _now()}


@app.post("/api/v1/gateway/stop", tags=["Gateway (OpenClaw)"], summary="Stop the gateway")
def gateway_stop(authorization: Optional[str] = Header(None)):
    global _gateway_running
    _gateway_running = False
    return {"status": "stopped", "timestamp": _now()}


@app.get("/api/v1/gateway/status", tags=["Gateway (OpenClaw)"], summary="Get gateway status")
def gateway_status(authorization: Optional[str] = Header(None)):
    return {
        "status": "running" if _gateway_running else "stopped",
        "service": "thannong-ai-mock",
        "version": "2.0.0",
        "active_sessions": len(_sessions),
        "timestamp": _now(),
    }


# ═════════════════════════════════════════════════════════════════════════════
# OPENCLAW-COMPATIBLE — SESSIONS
# ═════════════════════════════════════════════════════════════════════════════

@app.post("/api/v1/sessions/create", status_code=201, tags=["Sessions (OpenClaw)"],
          summary="Create a new session")
def oc_create_session(body: OpenClawCreateSessionRequest, authorization: Optional[str] = Header(None)):
    sid = body.sessionKey or str(uuid.uuid4())
    _sessions[sid] = {
        "meta": {"session_id": sid, "company_id": body.company_id or "",
                 "user_id": body.user_id or "",
                 "title": body.title or "New conversation", "created_at": _now()},
        "messages": []
    }
    return _sessions[sid]["meta"]


@app.get("/api/v1/sessions/list", tags=["Sessions (OpenClaw)"],
         summary="List active sessions")
def oc_list_sessions(authorization: Optional[str] = Header(None)):
    return {
        "sessions": [
            {**s["meta"], "message_count": len(s["messages"])}
            for s in _sessions.values()
        ],
        "total": len(_sessions),
    }


@app.post("/api/v1/sessions/send", tags=["Sessions (OpenClaw)"],
          summary="Send a message to a session")
def oc_send_message(body: OpenClawSendRequest, authorization: Optional[str] = Header(None)):
    s = _session(body.sessionKey)
    s["messages"].append({"message_id": str(uuid.uuid4()), "sender": "user",
                          "content": body.message, "timestamp": _now()})
    reply = random.choice(MOCK_RESPONSES)
    rid = str(uuid.uuid4())
    ts = _now()
    s["messages"].append({"message_id": rid, "sender": "assistant", "content": reply, "timestamp": ts})
    return {
        "message_id": rid,
        "sessionKey": body.sessionKey,
        "user_message": body.message,
        "reply": reply,
        "timestamp": ts,
    }


@app.get("/api/v1/sessions/{session_id}/history", tags=["Sessions (OpenClaw)"],
         summary="Get chat history for a session")
def oc_history(session_id: str, authorization: Optional[str] = Header(None)):
    if session_id not in _sessions:
        raise HTTPException(404, "Session not found")
    s = _sessions[session_id]
    return {"session_id": session_id, "messages": s["messages"]}


# ═════════════════════════════════════════════════════════════════════════════
# OPENAI-COMPATIBLE — CHAT COMPLETIONS
# ═════════════════════════════════════════════════════════════════════════════

@app.post("/v1/chat/completions", tags=["Chat Completions (OpenAI)"],
          summary="OpenAI-compatible chat completions (mock)")
def openai_chat_completions(body: OpenAIChatRequest, authorization: Optional[str] = Header(None)):
    # Extract the last user message
    user_msg = ""
    for m in reversed(body.messages):
        if m.role == "user":
            user_msg = m.content
            break

    reply = random.choice(MOCK_RESPONSES)
    completion_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"
    created = int(time.time())

    # Fake token counts
    prompt_tokens = sum(len(m.content.split()) for m in body.messages)
    completion_tokens = len(reply.split())

    return {
        "id": completion_id,
        "object": "chat.completion",
        "created": created,
        "model": body.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": reply,
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
        },
    }


