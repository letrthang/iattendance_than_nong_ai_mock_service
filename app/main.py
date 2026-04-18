import random
import uuid
from datetime import datetime, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.responses import MOCK_RESPONSES

app = FastAPI(
    title="Thần Nông AI — Mock Service",
    description=(
        "Mock API for iAttendance **Thần Nông AI**.\n\n"
        "Responses are randomly selected from a pool of **100 pre-written messages** "
        "covering iAttendance domains: attendance, leave, payslip, orders, farm, support, and more.\n\n"
        "**Base URL (production mock):** `https://iattendance-than-nong-ai-mock-service.onrender.com`"
    ),
    version="1.0.0",
    contact={"name": "iAttendance Team"},
    license_info={"name": "MIT"},
)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

tags_metadata = [
    {"name": "System", "description": "Health check and service info."},
    {"name": "Sessions", "description": "Create, retrieve, and delete chat sessions."},
    {"name": "Chat", "description": "Send a message and receive a random Thần Nông AI reply."},
]
app.openapi_tags = tags_metadata

_sessions: dict = {}


class CreateSessionRequest(BaseModel):
    company_id: str = Field(..., example="cmp-001")
    user_id: str = Field(..., example="usr-001")
    title: Optional[str] = Field("New conversation", example="Hỏi về chấm công")


class ChatRequest(BaseModel):
    session_id: str = Field(..., example="550e8400-e29b-41d4-a716-446655440000")
    company_id: str = Field(..., example="cmp-001")
    user_id: str = Field(..., example="usr-001")
    message: str = Field(..., example="Hôm nay tôi đã check-in chưa?")


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


@app.get("/health", tags=["System"], summary="Health check")
def health():
    return {"status": "ok", "service": "thannong-ai-mock", "version": "1.0.0", "timestamp": _now()}


@app.post("/api/sessions", status_code=201, tags=["Sessions"], summary="Create a new chat session")
def create_session(body: CreateSessionRequest):
    sid = str(uuid.uuid4())
    _sessions[sid] = {
        "meta": {"session_id": sid, "company_id": body.company_id, "user_id": body.user_id,
                 "title": body.title or "New conversation", "created_at": _now()},
        "messages": []
    }
    return _sessions[sid]["meta"]


@app.post("/api/chat", tags=["Chat"], summary="Send a message — get a random AI reply")
def chat(body: ChatRequest):
    s = _session(body.session_id, body.company_id, body.user_id)
    s["messages"].append({"message_id": str(uuid.uuid4()), "sender": "user",
                          "content": body.message, "timestamp": _now()})
    reply = random.choice(MOCK_RESPONSES)
    rid = str(uuid.uuid4())
    ts = _now()
    s["messages"].append({"message_id": rid, "sender": "assistant", "content": reply, "timestamp": ts})
    return {"message_id": rid, "session_id": body.session_id, "company_id": body.company_id,
            "user_id": body.user_id, "user_message": body.message, "reply": reply, "timestamp": ts}


@app.get("/api/sessions/{session_id}/history", tags=["Sessions"], summary="Get chat history for a session")
def history(session_id: str):
    if session_id not in _sessions:
        raise HTTPException(404, "Session not found")
    s = _sessions[session_id]
    return {"session_id": session_id, "company_id": s["meta"]["company_id"],
            "user_id": s["meta"]["user_id"], "messages": s["messages"]}


@app.delete("/api/sessions/{session_id}", status_code=204, tags=["Sessions"], summary="Delete a session")
def delete_session(session_id: str):
    _sessions.pop(session_id, None)
