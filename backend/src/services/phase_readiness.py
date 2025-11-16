"""Phase readiness data that reflects Phases 003-007."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass(slots=True)
class PhaseProgress:
    identifier: str
    phase: int
    title: str
    summary: str
    status: str
    requirements: List[str]
    delivered_capabilities: List[str]
    api_surface: List[str]
    last_synced_at: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class PhaseReadinessService:
    """In-memory representation of the readiness payload for phases 003-007."""

    def __init__(self) -> None:
        self._phase_progress = self._build_phase_progress()
        self._readiness_snapshot = self._build_readiness_snapshot()

    @staticmethod
    def _timestamp(hour: int) -> str:
        return datetime(2024, 5, 20, hour, tzinfo=timezone.utc).isoformat()

    def _build_phase_progress(self) -> List[PhaseProgress]:
        return [
            PhaseProgress(
                identifier="phase-003",
                phase=3,
                title="Market Research Synthesis",
                summary=(
                    "Implements the source trust panel, segment toggles, CTA macro, "
                    "model cache controls, and transparency export scaffolding."
                ),
                status="implemented",
                requirements=["FR-011", "FR-012", "FR-013", "FR-014", "FR-015"],
                delivered_capabilities=[
                    "trust_panel",
                    "segment_toggles",
                    "cta_macro",
                    "model_cache_control",
                    "transparency_exports",
                ],
                api_surface=[
                    "/phases/readiness#trust_panel",
                    "/phases/readiness#segments",
                    "/phases/readiness#model_cache",
                    "/phases/readiness#transparency_exports",
                ],
                last_synced_at=self._timestamp(9),
            ),
            PhaseProgress(
                identifier="phase-004",
                phase=4,
                title="Competitive Landscape Brief",
                summary=(
                    "Adds competitive diff snapshots, the rewrite template library, transparency "
                    "badges, partner widget samples, and the watch queue."
                ),
                status="implemented",
                requirements=["FR-016", "FR-017", "FR-018", "FR-019", "FR-020"],
                delivered_capabilities=[
                    "competitor_diff",
                    "template_library",
                    "transparency_badges",
                    "partner_widgets",
                    "competitor_watch",
                ],
                api_surface=[
                    "/phases/readiness#competitor_diff",
                    "/phases/readiness#template_library",
                    "/phases/readiness#partner_widgets",
                    "/phases/readiness#competitor_watch",
                ],
                last_synced_at=self._timestamp(10),
            ),
            PhaseProgress(
                identifier="phase-005",
                phase=5,
                title="Value Proposition Canvas",
                summary=(
                    "Delivers the rotating message tests, segment-based onboarding defaults, "
                    "shared CTA stack, partner evidence report, and template recommendations."
                ),
                status="implemented",
                requirements=["FR-021", "FR-022", "FR-023", "FR-024", "FR-025"],
                delivered_capabilities=[
                    "value_prop_tests",
                    "segment_onboarding",
                    "cta_stack",
                    "partner_reports",
                    "template_recommendations",
                ],
                api_surface=[
                    "/phases/readiness#value_props",
                    "/phases/readiness#segments",
                    "/phases/readiness#cta_stack",
                    "/phases/readiness#partner_reports",
                    "/phases/readiness#template_library",
                ],
                last_synced_at=self._timestamp(11),
            ),
            PhaseProgress(
                identifier="phase-006",
                phase=6,
                title="Success Metrics Blueprint",
                summary=(
                    "Exposes the KPI catalog, live curation batch stream, onboarding event schema, "
                    "badge quality alerts, and partner report tracker."
                ),
                status="implemented",
                requirements=["FR-026", "FR-027", "FR-028", "FR-029", "FR-030"],
                delivered_capabilities=[
                    "kpi_catalog",
                    "curation_stream",
                    "onboarding_schema",
                    "badge_alerts",
                    "report_tracker",
                ],
                api_surface=[
                    "/phases/readiness#kpi_catalog",
                    "/phases/readiness#curation_stream",
                    "/phases/readiness#onboarding_schema",
                    "/phases/readiness#badge_alerts",
                    "/phases/readiness#partner_reports",
                ],
                last_synced_at=self._timestamp(12),
            ),
            PhaseProgress(
                identifier="phase-007",
                phase=7,
                title="Content Category Architecture",
                summary=(
                    "Publishes category metadata, weekly production calendars, KPI tagging rules, "
                    "CTA defaults, and category performance dashboards."
                ),
                status="implemented",
                requirements=["FR-031", "FR-032", "FR-033", "FR-034", "FR-035"],
                delivered_capabilities=[
                    "category_metadata",
                    "production_calendar",
                    "kpi_tagging",
                    "cta_defaults",
                    "category_performance",
                ],
                api_surface=[
                    "/phases/readiness#categories",
                    "/phases/readiness#categories.calendar",
                    "/phases/readiness#categories.performance",
                ],
                last_synced_at=self._timestamp(13),
            ),
            PhaseProgress(
                identifier="phase-011",
                phase=11,
                title="Vision & Requirements Alignment",
                summary=(
                    "Consolidates KPI catalog guardrails, sponsor proof bundles, role-based "
                    "notifications, and telemetry hooks to feed Phases 012/018 backlog."
                ),
                status="documented",
                requirements=["FR-041", "FR-042", "FR-043", "FR-044", "FR-045"],
                delivered_capabilities=[
                    "role_based_notifications",
                    "sponsor_kpi_panel",
                    "onboarding_bridge",
                    "transparency_macro",
                    "guardrail_telemetry",
                ],
                api_surface=[
                    "/docs/records/phase-011/vision-and-requirements#fr-041",
                    "/docs/records/phase-011/vision-and-requirements#fr-042",
                    "/docs/records/phase-011/vision-and-requirements#fr-043",
                    "/docs/records/phase-011/vision-and-requirements#fr-044",
                    "/docs/records/phase-011/vision-and-requirements#fr-045",
                ],
                last_synced_at=self._timestamp(14),
            ),
        ]

    def _build_readiness_snapshot(self) -> Dict[str, Any]:
        return {
            "trust_panel": {
                "fields": [
                    "source_url",
                    "language_pair",
                    "model_name",
                    "inference_time_ms",
                    "reviewer",
                    "status",
                    "guardrail_notes",
                ],
                "cta_macro": {
                    "label": "View original",
                    "description": "Attach original link and rewrite rationale to every card.",
                    "footer_copy": "Rewritten for Korean punchlines per translation guardrails.",
                },
                "badge_states": [
                    {"state": "approved", "label": "Transparency badge", "color": "#34d399"},
                    {"state": "needs_review", "label": "Awaiting curator", "color": "#fcd34d"},
                ],
            },
            "segments": [
                {
                    "segment": "주니어 PM",
                    "persona": "Product generalist",
                    "pains": ["번역체", "맥락 부족"],
                    "gains": ["3분 내 이해", "원문 CTA"],
                    "toggles": ["Product Panic Room"],
                    "default_filters": ["Product Panic Room", "All-hands Catch-up"],
                    "onboarding_defaults": {
                        "notifications": ["AM digest"],
                        "categories": ["Product Panic Room"],
                    },
                },
                {
                    "segment": "시니어 마케터",
                    "persona": "Brand steward",
                    "pains": ["브랜드 안전성", "광고 피로"],
                    "gains": ["투명성 배지", "파트너 위젯"],
                    "toggles": ["Marketing Meme Board"],
                    "default_filters": ["Marketing Meme Board", "Exec Trend Roast"],
                    "onboarding_defaults": {
                        "notifications": ["Campaign alerts"],
                        "categories": ["Marketing Meme Board"],
                    },
                },
                {
                    "segment": "운영 큐레이터",
                    "persona": "Content ops",
                    "pains": ["검수 시간", "모델 재실행"],
                    "gains": ["템플릿 추천", "모델 캐시 제어"],
                    "toggles": ["Ops Laugh Lab"],
                    "default_filters": ["Ops Laugh Lab", "All-hands Catch-up"],
                    "onboarding_defaults": {
                        "notifications": ["Batch readiness"],
                        "categories": ["Ops Laugh Lab"],
                    },
                },
                {
                    "segment": "모바일 독자",
                    "persona": "On-the-go reader",
                    "pains": ["스크롤 피로", "광고 피로"],
                    "gains": ["카드형 UX", "원탭 공유"],
                    "toggles": ["Marketing Meme Board", "All-hands Catch-up"],
                    "default_filters": ["All-hands Catch-up"],
                    "onboarding_defaults": {
                        "notifications": ["Push personalization"],
                        "categories": ["All-hands Catch-up"],
                    },
                },
                {
                    "segment": "광고 파트너",
                    "persona": "Revenue stakeholder",
                    "pains": ["비용 불투명", "출처 우려"],
                    "gains": ["로컬 AI 비용 공개", "Transparency Export"],
                    "toggles": ["Exec Trend Roast"],
                    "default_filters": ["Exec Trend Roast", "Marketing Meme Board"],
                    "onboarding_defaults": {
                        "notifications": ["Weekly proof"],
                        "categories": ["Exec Trend Roast"],
                    },
                },
            ],
            "model_cache": {
                "modes": [
                    {
                        "id": "auto",
                        "label": "자동",
                        "description": "모델 추론 6초 SLA 내 자동 재실행",
                        "sla_seconds": 6,
                    },
                    {
                        "id": "on_demand",
                        "label": "온디맨드",
                        "description": "큐레이터가 필요 시 재실행",
                        "sla_seconds": 15,
                    },
                ],
                "cache_window_days": 30,
                "default_mode": "auto",
            },
            "transparency_exports": {
                "formats": [
                    {
                        "type": "csv",
                        "fields": ["log_id", "model", "reviewer", "status", "source_url"],
                    },
                    {
                        "type": "pdf",
                        "sections": ["executive_summary", "model_matrix", "guardrail_notes"],
                    },
                ],
                "delivery": {"cadence": "weekly", "channels": ["email", "s3"]},
            },
            "competitor_diff": {
                "categories": [
                    {
                        "category": "Transparency",
                        "newskoo": "로그/모델 전면 공개",
                        "competitors": "출처 미표기 또는 API 비공개",
                        "highlight": "유일한 투명성 배지",
                    },
                    {
                        "category": "템플릿",
                        "newskoo": "업계별 템플릿 6종",
                        "competitors": "모범 사례 없음",
                        "highlight": "큐레이터 처리량 20% 향상",
                    },
                    {
                        "category": "파트너 위젯",
                        "newskoo": "로그 포함 미니 피드",
                        "competitors": "딥링크 전용",
                        "highlight": "광고주 파일럿 4곳",
                    },
                ],
                "update_sla_days": 30,
            },
            "template_library": {
                "templates": [
                    {
                        "id": "ops-checklist",
                        "title": "Ops Laugh Lab Template",
                        "segments": ["운영 큐레이터"],
                        "tone": "체크리스트형 밈",
                        "macros": ["상황", "맥락", "한국식 punchline"],
                    },
                    {
                        "id": "product-story",
                        "title": "Product Panic Narrative",
                        "segments": ["주니어 PM"],
                        "tone": "스토리 카드",
                        "macros": ["문제", "실험", "교훈"],
                    },
                    {
                        "id": "marketing-slide",
                        "title": "Marketing Meme Board",
                        "segments": ["시니어 마케터", "광고 파트너"],
                        "tone": "슬라이드 카드",
                        "macros": ["후킹", "성과", "CTA"],
                    },
                ],
                "recommendations": {
                    "inputs": ["segment", "tone", "industry"],
                    "engine": "rule_based",
                },
            },
            "partner_widgets": {
                "variants": [
                    {
                        "id": "inline",
                        "description": "카드 3개 미니 피드",
                        "bundle_size": 3,
                    },
                    {
                        "id": "story",
                        "description": "스토리 하이라이트",
                        "bundle_size": 1,
                    },
                ],
                "embed_requirements": ["no external trackers", "load under 1s"],
            },
            "competitor_watch": {
                "tracked_competitors": 8,
                "alerts": [
                    {"name": "MemeDigest pricing", "status": "monitoring"},
                    {"name": "TLDR Biz mobile update", "status": "investigating"},
                ],
                "next_review": "2024-06-15",
            },
            "value_props": {
                "test_window_days": 14,
                "messages": [
                    {
                        "id": "transparency-first",
                        "copy": "Know which model touched every punchline.",
                        "segments": ["시니어 마케터", "광고 파트너"],
                    },
                    {
                        "id": "industry-memes",
                        "copy": "Instantly reuse industry-ready memes with context.",
                        "segments": ["주니어 PM", "운영 큐레이터"],
                    },
                    {
                        "id": "low-latency",
                        "copy": "Local AI costs under 100k KRW/month.",
                        "segments": ["광고 파트너"],
                    },
                ],
            },
            "cta_stack": {
                "channels": ["카카오", "Slack", "Email"],
                "badges": ["Transparency", "Value Prop"],
                "defaults": {
                    "ops": "Share checklist",
                    "product": "Open brief",
                    "marketing": "Book partner session",
                },
            },
            "partner_reports": {
                "formats": ["pdf", "csv"],
                "weekly_reports": 5,
                "tracker": [
                    {"partner": "Agency A", "status": "sent"},
                    {"partner": "Brand B", "status": "scheduled"},
                ],
            },
            "kpi_catalog": {
                "items": [
                    {
                        "metric": "월간 활성 직무 독자",
                        "type": "Lagging",
                        "target": "50k",
                        "source": "web/app events",
                    },
                    {
                        "metric": "세그먼트 온보딩 완료율",
                        "type": "Leading",
                        "target": "80%",
                        "source": "onboarding events",
                    },
                    {
                        "metric": "큐레이터 배치당 승인 카드 수",
                        "type": "Leading",
                        "target": "10",
                        "source": "검수 로그",
                    },
                    {
                        "metric": "출처 배지 노출률",
                        "type": "Leading",
                        "target": "99.5%",
                        "source": "퍼블리싱 로그",
                    },
                    {
                        "metric": "파트너 증빙 리포트 발송 수",
                        "type": "Lagging",
                        "target": "30/month",
                        "source": "로그 Export",
                    },
                ],
                "accuracy_tolerance": "±2%",
                "freshness": {"leading": "2h", "lagging": "24h"},
            },
            "curation_stream": {
                "last_batch_id": "BATCH-20240520-01",
                "avg_cards_per_batch": 10,
                "sla_minutes": 60,
                "recent_batches": [
                    {"id": "BATCH-20240519-02", "cards": 11, "badge_coverage": 1.0},
                    {"id": "BATCH-20240518-01", "cards": 9, "badge_coverage": 0.98},
                ],
            },
            "onboarding_schema": {
                "fields": [
                    {"name": "segment", "type": "string", "required": True},
                    {"name": "seniority", "type": "string", "required": True},
                    {"name": "channel", "type": "string", "required": False},
                ],
                "anonymization": "hash user ids, drop PII",
            },
            "badge_alerts": {
                "open_alerts": [
                    {"category": "Marketing Meme Board", "coverage": 0.97},
                ],
                "sla_minutes": 120,
                "notification_channels": ["Slack", "Email"],
            },
            "categories": {
                "metadata": [
                    {
                        "id": "ops-laugh-lab",
                        "title": "Ops Laugh Lab",
                        "tone": "체크리스트형 밈",
                        "cadence": "5/week",
                        "kpi_tags": ["curation_throughput", "badge_coverage"],
                        "default_push": "09:00 local",
                        "default_cta": "Share to Ops Slack",
                    },
                    {
                        "id": "product-panic-room",
                        "title": "Product Panic Room",
                        "tone": "스토리 카드",
                        "cadence": "5/week",
                        "kpi_tags": ["majr", "session_time"],
                        "default_push": "11:00 local",
                        "default_cta": "Open Product brief",
                    },
                    {
                        "id": "marketing-meme-board",
                        "title": "Marketing Meme Board",
                        "tone": "슬라이드 카드",
                        "cadence": "4/week",
                        "kpi_tags": ["share_rate", "partner_reports"],
                        "default_push": "13:00 local",
                        "default_cta": "Book partner session",
                    },
                    {
                        "id": "dev-standup-satires",
                        "title": "Dev Standup Satires",
                        "tone": "코드 스니펫",
                        "cadence": "3/week",
                        "kpi_tags": ["return_rate", "bug_reports"],
                        "default_push": "15:00 local",
                        "default_cta": "File bug roast",
                    },
                    {
                        "id": "exec-trend-roast",
                        "title": "Exec Trend Roast",
                        "tone": "인포그래픽",
                        "cadence": "2/week",
                        "kpi_tags": ["partner_reports", "revenue"],
                        "default_push": "Tuesday 08:00",
                        "default_cta": "Download proof deck",
                    },
                    {
                        "id": "all-hands-catch-up",
                        "title": "All-hands Catch-up",
                        "tone": "주간 요약",
                        "cadence": "1/week",
                        "kpi_tags": ["onboarding_completion", "push_ctr"],
                        "default_push": "Friday 17:00",
                        "default_cta": "Share recap",
                    },
                ],
                "calendar": [
                    {"day": "Mon", "slots": 3, "focus": ["Ops Laugh Lab", "Product Panic Room"]},
                    {"day": "Tue", "slots": 3, "focus": ["Marketing Meme Board", "Exec Trend Roast"]},
                    {"day": "Wed", "slots": 3, "focus": ["Dev Standup Satires", "Ops Laugh Lab"]},
                    {"day": "Thu", "slots": 3, "focus": ["Product Panic Room", "Marketing Meme Board"]},
                    {"day": "Fri", "slots": 2, "focus": ["All-hands Catch-up"]},
                ],
                "performance": {
                    "ops-laugh-lab": {"leading": "11 cards/batch", "lagging": "+8% ops CTR"},
                    "product-panic-room": {"leading": "48s avg dwell", "lagging": "+6% MAJR"},
                    "marketing-meme-board": {"leading": "34% share rate", "lagging": "+2 partner proofs"},
                    "dev-standup-satires": {"leading": "3 bug CTA/day", "lagging": "+5% dev return"},
                    "exec-trend-roast": {"leading": "2 reports/week", "lagging": "+1 enterprise lead"},
                    "all-hands-catch-up": {"leading": "82% push CTR", "lagging": "+4% onboarding"},
                },
            },
            "phase_011": {
                "focus": [
                    "role_based_notifications",
                    "sponsor_kpi_panel",
                    "guardrail_telemetry",
                ],
                "north_star": "월간 활성 직무 독자",
                "functional_requirements": ["FR-041", "FR-042", "FR-043", "FR-044", "FR-045"],
                "non_functional_requirements": ["NFR-025", "NFR-026", "NFR-027", "NFR-028"],
                "dependencies": [
                    "Phase 012 experiments",
                    "Phase 018 telemetry",
                    "Phase 019 sponsor workflow",
                ],
                "risks": [
                    {"id": "RSK-044", "mitigation": "Single template engine + QA checklist"},
                    {"id": "RSK-045", "mitigation": "KPI catalog sync + sponsor QA"},
                    {"id": "RSK-046", "mitigation": "GPU telemetry hooks + cache fallback"},
                ],
                "issues": ["#ISS-311", "#ISS-312", "#ISS-313", "#ISS-314", "#ISS-315", "#ISS-316", "#ISS-317", "#ISS-318", "#ISS-319"],
                "workshop": {
                    "attendees": 10,
                    "alignment_rate": 0.9,
                    "unresolved": [
                        "Exec pre-release scope pending Phase 012",
                        "Partner widget customization pending Phase 018",
                    ],
                },
            },
        }

    def list_phase_progress(self) -> List[Dict[str, Any]]:
        return [phase.to_dict() for phase in self._phase_progress]

    @property
    def readiness_snapshot(self) -> Dict[str, Any]:
        return self._readiness_snapshot


phase_readiness_service = PhaseReadinessService()
