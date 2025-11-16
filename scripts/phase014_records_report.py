"""Utility script that summarizes Phase 014 evidence artifacts."""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError as exc:  # pragma: no cover - import guard
    raise SystemExit(
        "PyYAML is required to run this script. Install dependencies via pip install -r backend/requirements.txt"
    ) from exc

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RECORDS_ROOT = REPO_ROOT / "docs/records/phase-014"


@dataclass(frozen=True)
class LandscapeSummary:
    competitor_count: int
    categories: Dict[str, int]
    regions: List[str]
    placeholders: int
    missing_metric_rows: int


@dataclass(frozen=True)
class ScorecardSummary:
    total_rows: int
    scored_rows: int
    incomplete_rows: int
    top_competitors: List[Dict[str, Any]]


@dataclass(frozen=True)
class WorkshopSummary:
    session: Optional[str]
    scheduled_at: Optional[str]
    facilitator: Optional[str]
    participant_count: int
    participants: List[str]
    action_item_count: int
    alignment_rate_target: Optional[float]
    action_items_target: Optional[int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize Phase 014 landscape, scorecard, and workshop artifacts"
    )
    parser.add_argument(
        "--records-root",
        type=Path,
        default=DEFAULT_RECORDS_ROOT,
        help="Path to docs/records/phase-014 (default: repository copy)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text)",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Missing YAML file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_landscape(records_root: Path) -> LandscapeSummary:
    data = load_yaml(records_root / "evidence/landscape/competitive-landscape.yaml")
    competitors = data.get("competitors", []) or []
    categories = Counter()
    regions = set()
    placeholders = 0
    missing_metrics = 0

    for competitor in competitors:
        name = str(competitor.get("name") or "").strip()
        if not name or name.upper() == "TBD":
            placeholders += 1
        category = competitor.get("category") or "unclassified"
        categories[category] += 1
        region = competitor.get("region_focus")
        if region:
            regions.add(region)

        traffic = competitor.get("traffic_monthly")
        retention = competitor.get("retention_90d")
        if traffic in (None, "") or retention in (None, ""):
            missing_metrics += 1

    return LandscapeSummary(
        competitor_count=len(competitors),
        categories=dict(sorted(categories.items())),
        regions=sorted(regions),
        placeholders=placeholders,
        missing_metric_rows=missing_metrics,
    )


def _to_float(value: Any) -> Optional[float]:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def load_scorecard(records_root: Path) -> ScorecardSummary:
    path = records_root / "evidence/scorecard/feature-value-scorecard.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing scorecard CSV: {path}")

    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not any(row.values()):
                continue
            rows.append(row)

    scored_rows = 0
    incomplete_rows = 0
    scored_entries: List[Dict[str, Any]] = []

    for row in rows:
        weights = [
            _to_float(row.get("function_weight")),
            _to_float(row.get("content_weight")),
            _to_float(row.get("brand_weight")),
            _to_float(row.get("revenue_weight")),
        ]
        scores = [
            _to_float(row.get("function_score")),
            _to_float(row.get("content_score")),
            _to_float(row.get("brand_score")),
            _to_float(row.get("revenue_score")),
        ]
        total_weight = sum(weight or 0 for weight in weights)
        weighted_score = 0.0
        valid_components = 0
        for weight, score in zip(weights, scores):
            if weight is None or score is None:
                continue
            weighted_score += weight * score
            valid_components += 1

        if valid_components and total_weight > 0:
            scored_rows += 1
            scored_entries.append(
                {
                    "competitor_id": row.get("competitor_id"),
                    "name": row.get("name"),
                    "weighted_score": round(weighted_score / total_weight, 2),
                    "story_hook": row.get("story_hook"),
                }
            )
        else:
            incomplete_rows += 1

    scored_entries.sort(key=lambda entry: entry["weighted_score"], reverse=True)
    return ScorecardSummary(
        total_rows=len(rows),
        scored_rows=scored_rows,
        incomplete_rows=incomplete_rows,
        top_competitors=scored_entries[:3],
    )


def load_workshop(records_root: Path) -> WorkshopSummary:
    path = records_root / "evidence/workshop/workshop-minutes.md"
    if not path.exists():
        raise FileNotFoundError(f"Missing workshop minutes: {path}")
    text = path.read_text(encoding="utf-8")
    data: Dict[str, Any] = {}
    if text.lstrip().startswith("---"):
        _, front_matter, *_ = text.split("---", 2)
        data = yaml.safe_load(front_matter) or {}
    else:
        data = yaml.safe_load(text) or {}

    participants = data.get("participants", []) or []
    success = data.get("success_criteria", {}) or {}
    return WorkshopSummary(
        session=data.get("session"),
        scheduled_at=data.get("scheduled_at"),
        facilitator=data.get("facilitator"),
        participant_count=len(participants),
        participants=[participant.get("name", "?") for participant in participants],
        action_item_count=len(data.get("action_items", []) or []),
        alignment_rate_target=success.get("alignment_rate_target"),
        action_items_target=success.get("action_items_min"),
    )


def build_summary(records_root: Path) -> Dict[str, Any]:
    landscape = load_landscape(records_root)
    scorecard = load_scorecard(records_root)
    workshop = load_workshop(records_root)
    return {
        "records_root": str(records_root),
        "landscape": landscape.__dict__,
        "scorecard": scorecard.__dict__,
        "workshop": workshop.__dict__,
    }


def format_text(summary: Dict[str, Any]) -> str:
    lines = ["Phase 014 Records Summary", f"Source: {summary['records_root']}"]

    landscape = summary["landscape"]
    lines.append(
        "\n[Landscape] "
        f"{landscape['competitor_count']} competitors across {len(landscape['categories'])} categories"
    )
    if landscape["regions"]:
        lines.append("  Regions: " + ", ".join(landscape["regions"]))
    lines.append("  Category breakdown:")
    for category, count in landscape["categories"].items():
        lines.append(f"    - {category}: {count}")
    lines.append(
        f"  Placeholder rows: {landscape['placeholders']} | Missing metric rows: {landscape['missing_metric_rows']}"
    )

    scorecard = summary["scorecard"]
    lines.append(
        "\n[Scorecard] "
        f"{scorecard['scored_rows']} scored / {scorecard['total_rows']} total rows"
    )
    lines.append(f"  Incomplete rows: {scorecard['incomplete_rows']}")
    if scorecard["top_competitors"]:
        lines.append("  Top competitors (weighted score):")
        for entry in scorecard["top_competitors"]:
            lines.append(
                f"    - {entry['name'] or entry['competitor_id']}: {entry['weighted_score']}"
                + (f" | Story hook: {entry['story_hook']}" if entry.get("story_hook") else "")
            )
    else:
        lines.append("  No scored competitors yet.")

    workshop = summary["workshop"]
    lines.append("\n[Workshop]")
    lines.append(
        f"  Session {workshop['session'] or 'n/a'} scheduled at {workshop['scheduled_at'] or 'n/a'}"
    )
    lines.append(f"  Facilitator: {workshop['facilitator'] or 'n/a'}")
    lines.append(
        f"  Participants ({workshop['participant_count']}): " + ", ".join(workshop["participants"])
    )
    lines.append(
        "  Success criteria → alignment rate target: "
        f"{workshop['alignment_rate_target']}, action items target: {workshop['action_items_target']}"
    )
    lines.append(f"  Captured action items: {workshop['action_item_count']}")

    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    summary = build_summary(args.records_root)
    if args.format == "json":
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print(format_text(summary))


if __name__ == "__main__":
    main()
