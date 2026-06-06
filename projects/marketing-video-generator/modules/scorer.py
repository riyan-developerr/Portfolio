import csv
from pathlib import Path
from datetime import datetime

import pandas as pd


RUNS_CSV = Path("data/runs.csv")

RUN_COLUMNS = [
    "run_id",
    "created_at",
    "product_name",
    "product_type",
    "prompt",
    "style",
    "backend_used",
    "duration",
    "product_visibility",
    "text_readability",
    "motion_smoothness",
    "style_match",
    "premium_look",
    "overall_quality",
    "average_score",
    "output_file",
    "plan_json_path",
    "notes",
    "status",
    "error_message"
]


SCORE_COLUMNS = [
    "product_visibility",
    "text_readability",
    "motion_smoothness",
    "style_match",
    "premium_look",
    "overall_quality"
]


def ensure_runs_csv(csv_path=RUNS_CSV):
    csv_path = Path(csv_path)
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    if csv_path.exists() and csv_path.stat().st_size > 0:
        with open(csv_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            current_header = next(reader, [])

        if current_header == RUN_COLUMNS:
            return

        backup_path = csv_path.with_name(
            f"runs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        csv_path.rename(backup_path)
        print(f"Old runs.csv backed up to: {backup_path}")

    with open(csv_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=RUN_COLUMNS)
        writer.writeheader()


def calculate_average_score(scores):
    values = []

    for column in SCORE_COLUMNS:
        value = scores.get(column, "")

        if value != "":
            values.append(float(value))

    if not values:
        return ""

    return round(sum(values) / len(values), 2)


def log_generation(
    run_id,
    product_name,
    product_type,
    prompt,
    style,
    backend_used,
    duration,
    output_file,
    plan_json_path,
    status="success",
    error_message="",
    notes=""
):
    ensure_runs_csv()

    row = {column: "" for column in RUN_COLUMNS}

    row.update({
        "run_id": run_id,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "product_name": product_name,
        "product_type": product_type,
        "prompt": prompt,
        "style": style,
        "backend_used": backend_used,
        "duration": duration,
        "output_file": output_file,
        "plan_json_path": plan_json_path,
        "notes": notes,
        "status": status,
        "error_message": error_message
    })

    with open(RUNS_CSV, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=RUN_COLUMNS)
        writer.writerow(row)


def update_score(run_id, scores, notes=""):
    ensure_runs_csv()

    df = pd.read_csv(RUNS_CSV, dtype={"run_id": str})
    run_id = str(run_id)

    if run_id not in df["run_id"].astype(str).values:
        return False, f"No run found with run_id: {run_id}"

    average_score = calculate_average_score(scores)

    mask = df["run_id"].astype(str) == run_id

    for column in SCORE_COLUMNS:
        df.loc[mask, column] = scores.get(column, "")

    df.loc[mask, "average_score"] = average_score
    df.loc[mask, "notes"] = notes

    df.to_csv(RUNS_CSV, index=False)

    return True, f"Score saved successfully. Average score: {average_score}"


def analyze_runs():
    ensure_runs_csv()

    df = pd.read_csv(RUNS_CSV)

    if df.empty:
        return "No runs found yet."

    scored_df = df.dropna(subset=["average_score"])

    if scored_df.empty:
        return "Runs exist, but no scores have been added yet."

    summary = scored_df.groupby("style")["average_score"].mean().sort_values(ascending=False)

    return summary


if __name__ == "__main__":
    ensure_runs_csv()
    print("Scorer module is ready.")
    print(analyze_runs())