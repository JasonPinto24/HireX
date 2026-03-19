import requests
import tempfile
import subprocess
from radon.complexity import cc_visit
from radon.metrics import mi_visit


def fetch_file_content(download_url: str) -> str:
    try:
        return requests.get(download_url, timeout=10).text
    except:
        return ""


def analyze_with_radon(code: str) -> dict:
    try:
        complexity_blocks = cc_visit(code)
        avg_complexity = (
            sum(block.complexity for block in complexity_blocks) / len(complexity_blocks)
            if complexity_blocks else 0
        )

        maintainability = mi_visit(code, multi=True)

        return {
            "complexity": avg_complexity,
            "maintainability": maintainability
        }
    except:
        return {"complexity": 0, "maintainability": 0}


def analyze_with_flake8(code: str) -> float:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode())
            tmp_path = tmp.name

        result = subprocess.run(
            ["flake8", tmp_path],
            capture_output=True,
            text=True
        )

        error_count = result.stdout.count("\n") if result.stdout else 0

        return max(0, 100 - error_count * 2)
    except:
        return 50  # fallback


def compute_code_quality_score(metrics: dict) -> float:
    complexity_score = max(0, 100 - metrics["complexity"] * 10)
    maintainability_score = metrics["maintainability"]
    lint_score = metrics["lint"]

    final = (
        0.4 * complexity_score +
        0.4 * maintainability_score +
        0.2 * lint_score
    )

    return round(final, 2)
def analyze_repository(repo: dict) -> float:
    contents_url = repo.get("contents_url", "").replace("{+path}", "")
    
    try:
        files = requests.get(contents_url, timeout=10).json()
    except:
        return 0

    scores = []
    count = 0

    for file in files:
        if file.get("name", "").endswith(".py"):
            code = fetch_file_content(file.get("download_url"))

            if not code.strip():
                continue

            radon_metrics = analyze_with_radon(code)
            lint_score = analyze_with_flake8(code)

            metrics = {
                "complexity": radon_metrics["complexity"],
                "maintainability": radon_metrics["maintainability"],
                "lint": lint_score
            }

            score = compute_code_quality_score(metrics)
            scores.append(score)

            count += 1
            if count >= 3:  # 🔥 limit for speed
                break

    return sum(scores) / len(scores) if scores else 0