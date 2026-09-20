"""
Initializes the Lifetime Data Log — the permanent, cumulative SQLite store
of every real benchmark call this project ever executes.

Two tables:
  - batches: one row per full benchmark sweep (metadata)
  - runs:    one row per single model call (the actual evidence)

Run this once to (re)create an empty skeleton. It is safe to re-run —
it will not touch existing data (uses CREATE TABLE IF NOT EXISTS).
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "lifetime_data_log.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS batches (
    batch_id    TEXT PRIMARY KEY,      -- e.g. "BATCH-01"
    date        TEXT NOT NULL,         -- ISO-8601 date the sweep was run
    trigger     TEXT NOT NULL,         -- why this sweep happened (e.g. "Phase 2 initial run")
    notes       TEXT                   -- anything specific to this batch
);

CREATE TABLE IF NOT EXISTS runs (
    run_id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id                    TEXT NOT NULL REFERENCES batches(batch_id),
    timestamp                   TEXT NOT NULL,      -- ISO-8601 datetime of the call
    pr_id                       TEXT NOT NULL,       -- e.g. "PR-01", from the curated dataset
    model_tier                  TEXT NOT NULL,       -- Frontier / Mid / Cheap / Open-source
    model_version               TEXT NOT NULL,       -- exact model string, e.g. "gemini-1.5-flash"
    tool_config                 TEXT NOT NULL,       -- e.g. "/review require_risk_assessment=true"
    raw_output_ref               TEXT,                -- generated review text, or a path/reference to it
    risk_level_output           TEXT,                -- PR-Agent's own field: low / medium / high
    merge_recommendation_output TEXT,                -- PR-Agent's own field
    judge_score                 REAL,                -- automated judge's score vs. rubric
    human_score                 REAL,                -- filled only for the ~20% calibration subsample
    matches_ground_truth        TEXT,                -- Y / N / Partial
    input_tokens                INTEGER,
    output_tokens                INTEGER,
    cost_usd                    REAL,                -- tokens x that provider's published price
    latency_ms                  INTEGER,
    anomaly_notes                TEXT                 -- errors, retries, rate-limit hits on this call
);
"""


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()
    print(f"Initialized (or confirmed) skeleton at: {DB_PATH}")


if __name__ == "__main__":
    init_db()
