# Thần Nông AI — Mock Service

> **Purpose:** A lightweight Python mock of the real Thần Nông AI service so that the iAttendance web app can be developed and tested end-to-end before the production AI is ready.
> No AI integration — responses are randomly selected from a pool of 100 pre-written messages covering the iAttendance domain.

---

## Architecture

```
Web App (iAttendance)
        |
        |  POST /api/chat
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
  "reply": "string  ← plain text OR Markdown — see important note below",
  "timestamp": "ISO-8601"
}
```

---

### ⚠️ Important for Web App Consumers — `reply` field format

The `reply` field returns either **plain text** or **Markdown** (randomly selected, 40/60 split):

| Type | Frequency | Example |
|------|-----------|---------|
| Plain text | 40 / 100 | `"Bạn đã check-in lúc 08:02 sáng nay."` |
| Markdown | 60 / 100 | `"## ✅ Check-in\n\n**Thời gian:** 08:02\n\n> Chúc bạn..."` |

**Your web app MUST render `reply` through a Markdown renderer.**
Plain text passes through a Markdown renderer unchanged, so one renderer handles both cases.

**Recommended renderer by framework:**

| Framework | Library |
|-----------|---------|
| React | `react-markdown` |
| Vue | `vue-markdown-render` |
| Angular | `ngx-markdown` |
| Vanilla JS | `marked.js` |

```jsx
// React — handles both plain text and Markdown automatically
import ReactMarkdown from 'react-markdown'

<ReactMarkdown>{message.reply}</ReactMarkdown>
```

**Note on newlines:** The `reply` string contains real newline characters (`\n`).
In the raw JSON response they appear as `\n` (standard JSON encoding) — this is expected.
After `fetch().then(r => r.json())` they become real newlines automatically. No manual string replacement needed.

---

### `GET /api/sessions/{session_id}/history`

Return all messages in a session (in-memory, resets on service restart).

**Response `200`**
```json
{
  "session_id": "uuid",
  "messages": [
    {
      "message_id": "uuid",
      "sender": "user | assistant",
      "content": "string (plain text OR Markdown)",
      "timestamp": "ISO-8601"
    }
  ]
}
```

---

## Testing the API

### From browser DevTools console

> ⚠️ Run from a **normal webpage tab** (e.g. `https://google.com`), **NOT** from a `chrome://` internal page.
> Chrome blocks external fetch requests from internal pages due to Content Security Policy (CSP).

Open any regular tab → DevTools (`F12`) → Console:

```javascript
fetch('https://iattendance-than-nong-ai-mock-service.onrender.com/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ session_id: 'test', company_id: 'c1', user_id: 'u1', message: 'hi' })
})
.then(r => r.json())
.then(data => console.log(data.reply))  // real newlines, ready for Markdown renderer
```

### From terminal

```bash
curl -s -X POST https://iattendance-than-nong-ai-mock-service.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"test","company_id":"c1","user_id":"u1","message":"hi"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['reply'])"
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
> Upgrade to a paid plan or add an uptime-ping cron if always-on is needed.

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
