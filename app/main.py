import random
import uuid
from datetime import datetime, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.responses import MOCK_RESPONSES
app = FastAPI(title="Than Nong AI - Mock Service", version="1.0.0")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)
_sessions: dict = {}
class CreateSessionRequest(BaseModel):
    company_id: str
    user_id: str
    title: Optional[str] = "New conversation"
class ChatRequest(BaseModel):
    session_id: str
    company_id: str
    user_id: str
    message: str
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
@app.get("/health")
def health():
    return {"status": "ok", "service": "thannong-ai-mock", "version": "1.0.0", "timestamp": _now()}
@app.post("/api/sessions", status_code=201)
def create_session(body: CreateSessionRequest):
    sid = str(uuid.uuid4())
    _sessions[sid] = {
        "meta": {"session_id": sid, "company_id": body.company_id, "user_id": body.user_id,
                 "title": body.title or "New conversation", "created_at": _now()},
        "messages": []
    }
    return _sessions[sid]["meta"]
@app.post("/api/chat")
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
@app.get("/api/sessions/{session_id}/history")
def history(session_id: str):
    if session_id not in _sessions:
        raise HTTPException(404, "Session not found")
    s = _sessions[session_id]
    return {"session_id": session_id, "company_id": s["meta"]["company_id"],
            "user_id": s["meta"]["user_id"], "messages": s["messages"]}
@app.delete("/api/sessions/{session_id}", status_code=204)
def delete_session(session_id: str):
    _sessions.pop(session_id, None)
