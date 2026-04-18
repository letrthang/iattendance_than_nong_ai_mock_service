# Thần Nông AI — Mock Service

> **Purpose:** A lightweight Python mock of the real Thần Nông AI service so that the iAttendance web app can be developed and tested end-to-end before the production AI is ready.
> No AI integration — responses are randomly selected from a pool of 100 pre-written messages covering the iAttendance domain.

---

## Architecture

```
Web App (iAttendance)
        │
        │  POST /api/chat
        ▼
┌──────────────────────────────────────┐
│  Mock Thần Nông AI Service (Python)  │
│  FastAPI  ·  Render.com (free tier)  │
│                                      │
│  • Returns 1 of 100 random replies   │
│  • Maintains in-memory session log   │
│  • CORS enabled for web app calls    │
└──────────────────────────────────────┘
        │
        ▼
  Public endpoint (Render.com)
  https://iattendance-than-nong-ai-mock-service.onrender.com
```

**Later swap**: When the real Thần Nông AI is ready, the web app only needs to change the base URL — the API contract is identical.

---

## Directory Structure

```
iattendance_than_nong_ai_mock_service/
├── app/
│   ├── main.py            ← FastAPI app, routes, CORS
│   └── responses.py       ← Pool of 100 random mock messages
├── .github/
│   └── workflows/
│       └── ci.yml         ← Lint + health-check on push
├── Dockerfile             ← Container image
├── render.yaml            ← Render.com one-click deploy config
├── requirements.txt       ← fastapi, uvicorn, pydantic
└── README.md              ← This file
```

---

## API Contract

All endpoints live under the same base URL.  
The contract **matches the real Thần Nông AI** so no web-app changes are needed at cutover.

### `GET /health`
Health check.

**Response `200`**
```json
{ "status": "ok", "service": "thannong-ai-mock", "version": "1.0.0" }
```

---

### `POST /api/sessions`
Create a new chat session.

**Request body**
```json
{
  "company_id": "string",
  "user_id": "string",
  "title": "string (optional)"
}
```

**Response `201`**
```json
{
  "session_id": "uuid",
  "company_id": "string",
  "user_id": "string",
  "title": "string",
  "created_at": "ISO-8601"
}
```

---

### `POST /api/chat`
Send a message and receive a mock AI reply.

**Request body**
```json
{
  "session_id": "uuid",
  "company_id": "string",
  "user_id": "string",
  "message": "string"
}
```

**Response `200`**
```json
{
  "message_id": "uuid",
  "session_id": "uuid",
  "company_id": "string",
  "user_id": "string",
  "user_message": "string",
  "reply": "string",
  "timestamp": "ISO-8601"
}
```

---

### `GET /api/sessions/{session_id}/history`
Return all messages in a session (in-memory, resets on restart).

**Response `200`**
```json
{
  "session_id": "uuid",
  "messages": [
    {
      "message_id": "uuid",
      "sender": "user | assistant",
      "content": "string",
      "timestamp": "ISO-8601"
    }
  ]
}
```

---

## Deploy to Render.com (free tier)

Render auto-deploys from GitHub on every push to `main`.

### One-time setup
1. Go to [https://render.com](https://render.com) → **New Web Service**
2. Connect this GitHub repo
3. Render detects `render.yaml` automatically → click **Apply**
4. Service is live at `https://iattendance-thannong-ai-mock.onrender.com`

### Manual deploy trigger
```bash
# Just push to main — Render picks it up automatically
git push origin main
```

### Verify
```bash
curl https://iattendance-than-nong-ai-mock-service.onrender.com/health

curl -X POST https://iattendance-than-nong-ai-mock-service.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"test-123","company_id":"cmp-1","user_id":"usr-1","message":"Xin chào"}'
```

---

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Health check
curl http://localhost:8000/health

# Chat
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"local-1","company_id":"cmp-1","user_id":"usr-1","message":"Hello"}'
```

---

## Mock Responses Coverage

The 100 pre-written responses cover the following iAttendance domains:

| Domain | # responses |
|---|---|
| Attendance / check-in / check-out | 15 |
| Leave management | 12 |
| Payslip & salary | 10 |
| Orders & revenue | 10 |
| Farm management | 8 |
| Customer support tickets | 8 |
| Assets & devices | 7 |
| Visitors | 5 |
| General greetings & small-talk | 15 |
| Errors / unknown queries | 10 |
| **Total** | **100** |

---

## Public Endpoint

| Environment | URL |
|---|---|
| **Production mock** | `https://iattendance-than-nong-ai-mock-service.onrender.com` |
| **Swagger UI** | `https://iattendance-than-nong-ai-mock-service.onrender.com/docs` |
| **ReDoc** | `https://iattendance-than-nong-ai-mock-service.onrender.com/redoc` |
| **OpenAPI JSON** | `https://iattendance-than-nong-ai-mock-service.onrender.com/openapi.json` |
| Local dev | `http://localhost:8000` |
| Local Swagger UI | `http://localhost:8000/docs` |

> ⚠️ Render free tier **spins down after 15 min of inactivity** — first request after idle takes ~30s to cold-start.  
> Upgrade to a paid plan or add an uptime-ping cron if always-on is needed.

---

## Swap to Real Thần Nông AI

When the real service is ready, update the web app's base URL env var:

```env
# .env (web app)
# Before (mock)
THANNONG_AI_BASE_URL=https://iattendance-than-nong-ai-mock-service.onrender.com

# After (real)
THANNONG_AI_BASE_URL=https://thannong-ai.your-domain.com
```

No other changes needed — the API contract is identical.

