#!/usr/bin/env bash
if [ ! -f "./db/loaded" ]; then
  touch "./db/loaded"
  python3 -m db.load_data
fi

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000