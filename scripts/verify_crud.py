"""
One-off verification that Create/Read/Update/Delete all work against the
Lifetime Data Log skeleton. Inserts a dummy batch + run, reads it back,
updates it, deletes it, and confirms the tables end up empty again —
proving CRUD works without leaving any fake data behind.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "lifetime_data_log.db"


def run():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # --- CREATE ---
    cur.execute(
        "INSERT INTO batches (batch_id, date, trigger, notes) VALUES (?, ?, ?, ?)",
        ("TEST-BATCH", "2026-09-20", "CRUD verification (dummy, will be deleted)", None),
    )
    cur.execute(
        """INSERT INTO runs (batch_id, timestamp, pr_id, model_tier, model_version,
                              tool_config, judge_score, input_tokens, output_tokens,
                              cost_usd, latency_ms)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        ("TEST-BATCH", "2026-09-20T00:00:00", "PR-TEST", "Cheap", "test-model-v0",
         "/review", 0.5, 100, 50, 0.0001, 500),
    )
    conn.commit()
    print("CREATE: inserted 1 batch row + 1 run row")

    # --- READ ---
    cur.execute("SELECT run_id, pr_id, judge_score FROM runs WHERE batch_id = 'TEST-BATCH'")
    row = cur.fetchone()
    print(f"READ:   fetched row -> run_id={row[0]}, pr_id={row[1]}, judge_score={row[2]}")
    run_id = row[0]

    # --- UPDATE ---
    cur.execute("UPDATE runs SET judge_score = ? WHERE run_id = ?", (0.9, run_id))
    conn.commit()
    cur.execute("SELECT judge_score FROM runs WHERE run_id = ?", (run_id,))
    print(f"UPDATE: judge_score is now {cur.fetchone()[0]} (was 0.5)")

    # --- DELETE (cleanup, so the skeleton stays empty) ---
    cur.execute("DELETE FROM runs WHERE batch_id = 'TEST-BATCH'")
    cur.execute("DELETE FROM batches WHERE batch_id = 'TEST-BATCH'")
    conn.commit()
    print("DELETE: removed the dummy rows")

    # --- CONFIRM CLEAN SKELETON ---
    cur.execute("SELECT COUNT(*) FROM runs")
    runs_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM batches")
    batches_count = cur.fetchone()[0]
    print(f"VERIFY: runs table has {runs_count} rows, batches table has {batches_count} rows (both should be 0)")

    conn.close()
    assert runs_count == 0 and batches_count == 0, "Cleanup failed -- skeleton is not empty!"
    print("\nAll CRUD operations verified successfully. Skeleton is clean.")


if __name__ == "__main__":
    run()
