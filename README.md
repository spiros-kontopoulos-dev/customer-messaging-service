# Restaurant Messaging Service

Small Python service used for a production-debugging exercise. It models a restaurant messaging agent that can recognize a customer's "usual" order and suggest a reorder.

## Requirements

- Python 3.14
- Docker + Docker Compose
- PostgreSQL 15 (provided by Docker)

## Setup

```bash
cp .env.example .env
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
docker compose up -d db
python scripts/init_db.py
python scripts/seed.py
```

Run the app:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest -q
```

Useful commands:

```bash
docker compose ps
docker compose logs db
git status
git diff
```

## API

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Send a customer message:

```bash
curl -X POST http://127.0.0.1:8000/stores/1/messages \
  -H 'Content-Type: application/json' \
  -d '{"phone":"+15550001111","message":"my usual"}'
```

See `INTERVIEW_TASK.md` for the production issue.
