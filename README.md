# Thần Nông AI — Mock Service

> **Purpose:** A lightweight Python mock of the real Thần Nông AI service so that the iAttendance web app can be developed and tested end-to-end before the production AI is ready.
> No AI integration — responses are randomly selected from a pool of 100 pre-written messages covering the iAttendance domain.

---
> **Swagger UI:** https://iattendance-than-nong-ai-mock-service.onrender.com/docs

> ⚠️ **Note:** The service will spin down after **15 minutes of inactivity**. The first request after idle may take ~30s to cold-start.

---

## Architecture

```
Web App (iAttendance) / External Services
        |
        |  OpenClaw API  ──  /api/v1/sessions/*  /api/v1/gateway/*
        |  OpenAI API    ──  /v1/chat/completions
        v
+--------------------------------------+
|  Mock Than Nong AI Service (Python)  |
|  FastAPI  .  Render.com (free tier)  |
|                                      |
|  . Returns 1 of 100 random replies   |
|  . Maintains in-memory session log   |
|  . CORS enabled for web app calls    |
+--------------------------------------+
        |
        v
  Public endpoint (Render.com)
  https://iattendance-than-nong-ai-mock-service.onrender.com
```

**Later swap**: When the real Thần Nông AI is ready, the web app only needs to change the base URL — the API contract is identical.

---

## API Groups

| Group | Prefix | Description |
|-------|--------|-------------|
| **OpenClaw-compatible** | `/api/v1/gateway/*`, `/api/v1/sessions/*` | Session management and messaging (OpenClaw spec) |
| **OpenAI-compatible** | `/v1/chat/completions` | Drop-in replacement for OpenAI Chat Completions API |

**Authentication:** All endpoints accept `Authorization: Bearer <token>` header. The mock server does not validate tokens — all requests are allowed.

---

## API Contract

### 🔧 System

#### `GET /health`

Health check.

**Response `200`**
```json
{ "status": "ok", "service": "thannong-ai-mock", "version": "2.0.0" }
```

---

### 🌐 OpenClaw-Compatible — Gateway

#### `POST /api/v1/gateway/start`

Start the gateway.

**Response `200`**
```json
{ "status": "started", "timestamp": "ISO-8601" }
```

#### `POST /api/v1/gateway/stop`

Stop the gateway.

**Response `200`**
```json
{ "status": "stopped", "timestamp": "ISO-8601" }
```

#### `GET /api/v1/gateway/status`

Get gateway status.

**Response `200`**
```json
{
  "status": "running",
  "service": "thannong-ai-mock",
  "version": "2.0.0",
  "active_sessions": 1,
  "timestamp": "ISO-8601"
}
```

---

### 🌐 OpenClaw-Compatible — Sessions

#### `POST /api/v1/sessions/create`

Create a new session.

**Request body**
```json
{
  "sessionKey": "main",
  "company_id": "string (optional)",
  "user_id": "string (optional)",
  "title": "string (optional)"
}
```

**Response `201`**
```json
{
  "session_id": "main",
  "company_id": "string",
  "user_id": "string",
  "title": "string",
  "created_at": "ISO-8601"
}
```

#### `GET /api/v1/sessions/list`

List active sessions.

**Response `200`**
```json
{
  "sessions": [
    {
      "session_id": "main",
      "company_id": "string",
      "user_id": "string",
      "title": "string",
      "created_at": "ISO-8601",
      "message_count": 2
    }
  ],
  "total": 1
}
```

#### `POST /api/v1/sessions/send`

Send a message to a session.

**Request body**
```json
{
  "sessionKey": "main",
  "message": "Hello from external service!"
}
```

**Response `200`**
```json
{
  "message_id": "uuid",
  "sessionKey": "main",
  "user_message": "string",
  "reply": "string  ← plain text OR Markdown",
  "timestamp": "ISO-8601"
}
```

#### `GET /api/v1/sessions/{session_id}/history`

Return all messages in a session.

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

### 🤖 OpenAI-Compatible — Chat Completions

#### `POST /v1/chat/completions`

Accepts the same request format as OpenAI's Chat Completions API.

**Request body**
```json
{
  "model": "deepseek/deepseek-chat",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "temperature": 0.7,
  "max_tokens": 100
}
```

**Response `200`**
```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "deepseek/deepseek-chat",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 9,
    "total_tokens": 19
  }
}
```

**Authentication:** Pass `Authorization: Bearer YOUR_API_KEY` header (accepted but not validated in mock).

**Supported parameters:** `model`, `messages`, `temperature`, `max_tokens`, `stream` (accepted but ignored), `top_p`, `frequency_penalty`, `presence_penalty`, `stop`.

---

### ⚠️ Important for Web App Consumers — `reply` / `content` field format

The reply field returns either **plain text** or **Markdown** (randomly selected, 40/60 split):

| Type | Frequency | Example |
|------|-----------|---------|
| Plain text | 40 / 100 | `"Bạn đã check-in lúc 08:02 sáng nay."` |
| Markdown | 60 / 100 | `"## ✅ Check-in\n\n**Thời gian:** 08:02\n\n> Chúc bạn..."` |

**Your web app MUST render through a Markdown renderer.** Plain text passes through unchanged.

**Recommended renderer by framework:**

| Framework | Library |
|-----------|---------|
| React | `react-markdown` |
| Vue | `vue-markdown-render` |
| Angular | `ngx-markdown` |
| Vanilla JS | `marked.js` |

---


## Testing the API

### OpenClaw — Send a message

```bash
curl -X POST \
  https://iattendance-than-nong-ai-mock-service.onrender.com/api/v1/sessions/send \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sessionKey": "main",
    "message": "Hello from external service!"
  }'
```

### OpenAI — Chat Completions

```bash
curl -X POST \
  https://iattendance-than-nong-ai-mock-service.onrender.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-chat",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
  }'
```

### From browser DevTools console

```javascript
// OpenAI-compatible
fetch('https://iattendance-than-nong-ai-mock-service.onrender.com/v1/chat/completions', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer test' },
  body: JSON.stringify({
    model: 'thannong-ai-mock',
    messages: [{ role: 'user', content: 'Xin chào' }]
  })
})
.then(r => r.json())
.then(data => console.log(data.choices[0].message.content))
```

---

## Deploy to Render.com (free tier)

Render auto-deploys from GitHub on every push to `main`.

### One-time setup
1. Go to [https://render.com](https://render.com) → **New Web Service**
2. Connect this GitHub repo
3. Render detects `render.yaml` automatically → click **Apply**
4. Service is live at `https://iattendance-than-nong-ai-mock-service.onrender.com`

### Verify
```bash
curl https://iattendance-than-nong-ai-mock-service.onrender.com/health

curl -X POST https://iattendance-than-nong-ai-mock-service.onrender.com/api/v1/sessions/send \
  -H "Content-Type: application/json" \
  -d '{"sessionKey":"test","message":"Xin chào"}'
```

---

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Health check
curl http://localhost:8000/health

# OpenClaw — send message
curl -X POST http://localhost:8000/api/v1/sessions/send \
  -H "Content-Type: application/json" \
  -d '{"sessionKey":"test","message":"Hello"}'

# OpenAI — chat completions
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"test","messages":[{"role":"user","content":"Hello"}]}'
```

---

## Mock Responses Coverage

| Domain | Format | # |
|--------|--------|---|
| Attendance / check-in / check-out | Markdown | 12 |
| Leave management | Markdown | 10 |
| Payslip & salary | Markdown | 10 |
| Orders & revenue | Markdown | 8 |
| Farm management | Markdown | 8 |
| Support, visitors & general | Markdown | 12 |
| All domains mixed | Plain text | 40 |
| **Total** | | **100** |

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

---

## Swap to Real Thần Nông AI

When the real service is ready, update the web app base URL env var:

```env
# Before (mock)
THANNONG_AI_BASE_URL=https://iattendance-than-nong-ai-mock-service.onrender.com

# After (real)
THANNONG_AI_BASE_URL=https://thannong-ai.your-domain.com
```

No other changes needed — the API contract is identical.
