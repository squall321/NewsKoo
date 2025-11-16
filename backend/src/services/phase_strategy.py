"""Phase strategy payload for phases 014-020."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Tuple


PhaseRange = Tuple[int, int]


@dataclass(slots=True)
class PhaseTask:
    """Represents a major task within a phase plan."""

    name: str
    description: str
    checkpoints: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PhasePlan:
    """Structured payload that mirrors the phase planning docs."""

    identifier: str
    phase: int
    title: str
    objective: str
    storage_path: str
    tasks: List[PhaseTask]
    deliverables: List[str]
    success_metrics: List[str]
    timeline: List[Dict[str, str]]
    dependencies: List[str]
    guardrails: Dict[str, str]

    def to_dict(self) -> Dict[str, Any]:
        payload = asdict(self)
        payload["tasks"] = [task.to_dict() for task in self.tasks]
        return payload


class PhaseStrategyService:
    """In-memory plan representation for phase strategy payloads."""

    _GUARDRAILS = {
        "reference_doc": "docs/strategy/translation-guardrails.md",
        "cost_policy": "저비용·로컬 AI 우선 원칙 준수",
        "translation_policy": "상용 번역 API 기본 비활성, 사용 시 비용/위험 명시",
        "model_preference": "16GB VRAM RTX 5070 Ti 환경에서 실행 가능한 Hugging Face + QLoRA/양자화 모델",  # noqa: E501
        "source_policy": "Reddit 등 원천은 NewsKoo 톤으로 재작성하고 저작권/약관 준수 로그를 남긴다.",
    }

    def __init__(self) -> None:
        self._plans_by_range = self._build_plans_by_range()

    def _build_plans_by_range(self) -> Dict[PhaseRange, List[PhasePlan]]:
        return {
            (14, 20): self._build_strategy_plans(),
            (21, 27): self._build_architecture_plans(),
        }

    def _build_strategy_plans(self) -> List[PhasePlan]:
        return [
            PhasePlan(
                identifier="phase-014",
                phase=14,
                title="경쟁 구도 인텔리전스",
                objective=(
                    "경쟁사·대체재·잠재 진입자를 포함한 경쟁 구도를 정밀 분석해 비전 문구와 "
                    "핵심 가치표를 재정의하고 phase-015~020 백로그의 근거를 다진다."
                ),
                storage_path="docs/records/phase-014/",
                tasks=[
                    PhaseTask(
                        name="데이터 기반 경쟁 인벤토리",
                        description=(
                            "SimilarWeb/SensorTower/공개 IR 자료의 트래픽, 잔존율, 수익 모델 데이터를 모아 "
                            "정량 비교표를 만든다. 커뮤니티·SNS 피드백은 AI 요약으로 톤·UX 패턴을 라벨링한다."
                        ),
                        checkpoints=[
                            "정량/정성 소스 목록 확정",
                            "원천 데이터 증적을 공유 드라이브에 업로드",
                        ],
                    ),
                    PhaseTask(
                        name="벤치마크 프레임워크",
                        description="기능/콘텐츠/브랜드/수익 4개 축 Scorecard와 SWOT, Feature-Value Matrix를 제작한다.",
                        checkpoints=[
                            "색상/아이콘으로 리스크·기회 표시",
                            "Matrix 내 phase-015~020 의존성 주석",
                        ],
                    ),
                    PhaseTask(
                        name="시나리오 워크숍",
                        description="PM·콘텐츠·BizDev 워크숍에서 방어/공격/협력 시나리오 3종과 필요 역량을 합의한다.",
                        checkpoints=[
                            "참석자 합의율 90% 이상 기록",
                            "Needs-Decision 항목을 Jira issue로 백필",
                        ],
                    ),
                    PhaseTask(
                        name="백로그·리스크 연동",
                        description="Phase 015~020 관련 의존성과 경쟁사별 리스크를 Issue Tracker·Risk Register에 링크한다.",
                        checkpoints=[
                            "리스크 Severity/Probability 태깅",
                            "phase-019 Heat Map 입력값 전달",
                        ],
                    ),
                ],
                deliverables=[
                    "경쟁사 Landscape 보고서 + 데이터 시트",
                    "Scorecard, SWOT, Feature-Value Matrix",
                    "워크숍 회의록과 후속 백로그",
                ],
                success_metrics=[
                    "주요 경쟁사/대체재 10곳 이상 커버",
                    "워크숍 합의율 90% 이상 & 액션 5건 도출",
                    "리스크 레지스터 신규 리스크 5건 이상",
                ],
                timeline=[
                    {"day": "D1-D2", "focus": "데이터 수집/정리, 증적 업로드"},
                    {"day": "D3", "focus": "Scorecard/Matrix 초안 및 Slack 리뷰"},
                    {"day": "D4", "focus": "워크숍 개최 및 결정사항 기록"},
                    {"day": "D5", "focus": "문서 QA, 번역 검수 후 phase-015 전달"},
                ],
                dependencies=["Phase 015 Value Proposition", "Phase 019 Risk Register"],
                guardrails=self._GUARDRAILS,
            ),
            PhasePlan(
                identifier="phase-015",
                phase=15,
                title="가치 제안 정교화",
                objective=(
                    "핵심 사용자 세그먼트가 체감할 가치 제안을 언어·비주얼·서비스 레벨로 구체화해 "
                    "경쟁 대비 차별성을 명문화하고 다음 페이즈의 메시징/실험에 입력한다."
                ),
                storage_path="docs/records/phase-015/",
                tasks=[
                    PhaseTask(
                        name="페인 포인트 재검증",
                        description="Phase 013~014 리서치를 인터뷰·설문으로 재평가하고 JTBD/Value Proposition Canvas를 채운다.",
                        checkpoints=[
                            "세그먼트 3개 Pain/Gain/Jobs 100% 작성",
                            "익명화한 인터뷰 데이터 정리",
                        ],
                    ),
                    PhaseTask(
                        name="차별 가치 패키지",
                        description="콘텐츠 큐레이션·로컬라이징 품질·커뮤니티 신뢰 등 가치 테마별 Feature/Proof/Benefit를 문서화한다.",
                        checkpoints=[
                            "Messaging Pillar에 텍스트·비주얼 레퍼런스 수록",
                            "Glossary와 용어 동기화",
                        ],
                    ),
                    PhaseTask(
                        name="실험 가설 & MVP",
                        description="A/B 또는 Concierge MVP 가설 2건 이상 정의하고 성공/실패 시나리오, KPI, 의존 페이즈를 표로 정리한다.",
                        checkpoints=[
                            "실험 백로그 티켓 작성",
                            "데이터 수집 계획 첨부",
                        ],
                    ),
                    PhaseTask(
                        name="경영진 리뷰",
                        description="C-level·콘텐츠 리드 리뷰 미팅으로 스토리라인을 검증하고 Feedback Log/Jira 티켓을 남긴다.",
                        checkpoints=[
                            "Rework 요청 10% 이하",
                            "피드백 48시간 내 반영",
                        ],
                    ),
                ],
                deliverables=[
                    "세그먼트별 Value Proposition Canvas & JTBD 카드",
                    "Messaging Pillar, 예시 카피/비주얼",
                    "실험 가설 표와 KPI/의존성 맵",
                ],
                success_metrics=[
                    "핵심 세그먼트 3개 Canvas 완성",
                    "경영진 리뷰 Rework 10% 이하",
                    "가설 2건 이상 실험 백로그 등록",
                ],
                timeline=[
                    {"day": "D1", "focus": "기존 리서치 정리, 인터뷰 스크립트 확정"},
                    {"day": "D2-D3", "focus": "인터뷰/설문, Canvas 작성"},
                    {"day": "D4", "focus": "Messaging Pillar와 가설 정리"},
                    {"day": "D5", "focus": "리뷰 미팅 및 피드백 반영"},
                ],
                dependencies=["Phase 016 KPI Blueprint", "Phase 017 Category design"],
                guardrails=self._GUARDRAILS,
            ),
            PhasePlan(
                identifier="phase-016",
                phase=16,
                title="KPI 거버넌스",
                objective=(
                    "전략 목표 달성 여부를 실시간 판단할 지표 체계를 구축해 이후 모든 페이즈의 우선순위와 "
                    "Alert 룰을 뒷받침한다."
                ),
                storage_path="docs/records/phase-016/",
                tasks=[
                    PhaseTask(
                        name="지표 후보 도출",
                        description="North Star, 입력 지표, 품질/리스크 지표 후보 20개 이상을 수집해 목적/데이터 소스를 문서화한다.",
                        checkpoints=[
                            "지표 템플릿에 목적/결정/업데이트 빈도 기입",
                            "측정 불가 항목은 프록시 제안",
                        ],
                    ),
                    PhaseTask(
                        name="데이터 가능성 검토",
                        description="GA4/Mixpanel/Superset 등 기존 스택과 로그 스키마를 점검해 수집 가능성·정확도를 평가한다.",
                        checkpoints=[
                            "Analytics 팀 인터뷰 완료",
                            "기술 부채 티켓 생성",
                        ],
                    ),
                    PhaseTask(
                        name="KPI 트리 & 대시보드",
                        description="비전→전략→팀 KPI→실험 지표 트리를 시각화하고 Looker Studio/Figma 와이어프레임을 만든다.",
                        checkpoints=[
                            "우선 지표 8개 선정",
                            "Alert 임계값 초안 작성",
                        ],
                    ),
                    PhaseTask(
                        name="거버넌스 플랜",
                        description="데이터 오너, 업데이트 주기, 품질 체크, 경보 룰을 문서화해 리스크 레지스터와 연동한다.",
                        checkpoints=[
                            "Alert 룰 4건 이상 정의",
                            "phase-019 연계 포인트 기록",
                        ],
                    ),
                ],
                deliverables=[
                    "KPI 후보 목록/평가표",
                    "KPI 트리 다이어그램 & 대시보드 와이어",
                    "거버넌스/Alert 정의서",
                ],
                success_metrics=[
                    "최종 지표 12개 이하 + 소스/주기 명시",
                    "대시보드 와이어 데이터·제품 리드 2명 승인",
                    "Alert 룰 4건 이상 리스크 레지스터 연동",
                ],
                timeline=[
                    {"day": "D1", "focus": "지표 브레인스토밍, 데이터 인벤토리"},
                    {"day": "D2", "focus": "데이터 수집 가능성 검토"},
                    {"day": "D3", "focus": "KPI 트리, 대시보드 와이어 제작"},
                    {"day": "D4", "focus": "거버넌스/Alert 정의 및 리뷰"},
                    {"day": "D5", "focus": "피드백 반영, phase-017 핸드오프"},
                ],
                dependencies=["Phase 017 Category prioritisation", "Phase 018 revenue KPIs"],
                guardrails=self._GUARDRAILS,
            ),
            PhasePlan(
                identifier="phase-017",
                phase=17,
                title="콘텐츠 카테고리 설계",
                objective=(
                    "콘텐츠 카테고리 구조를 사용자 니즈·비즈니스 가치·제작 역량 관점에서 최적화해 제품 맵과 "
                    "에디토리얼 캘린더의 토대를 마련한다."
                ),
                storage_path="docs/records/phase-017/",
                tasks=[
                    PhaseTask(
                        name="카테고리 후보 수집",
                        description="Phase 013~016 인사이트와 경쟁사 분석을 묶어 거시/미시 주제를 발산하고 사용자 여정 단계에 맵핑한다.",
                        checkpoints=[
                            "발견→소화→공유 단계별 요구 정리",
                            "톤/윤리 리스크 주석",
                        ],
                    ),
                    PhaseTask(
                        name="우선순위 매트릭스",
                        description="임팩트 vs 실행 난이도 Scoring Matrix로 6~8개 핵심 카테고리를 선정하고 AI/윤리 속성을 태깅한다.",
                        checkpoints=[
                            "점수 산출 근거 기록",
                            "데이터팀 SLA 참고",
                        ],
                    ),
                    PhaseTask(
                        name="운영 가이드 템플릿",
                        description="카테고리별 톤/포맷/빈도/KPI/데이터 소스를 표준 템플릿으로 작성하고 Swimlane으로 파이프라인을 시각화한다.",
                        checkpoints=[
                            "샘플 완성본 2개",
                            "Swimlane 버전 관리",
                        ],
                    ),
                    PhaseTask(
                        name="워크숍 & PoC",
                        description="에디터·데이터 저널리스트·PM 워크숍으로 정의서를 검증하고 실험할 2개 카테고리 PoC 계획을 만든다.",
                        checkpoints=[
                            "Must Fix 피드백 3건 이하",
                            "PoC 범위/리소스/KPI 명시",
                        ],
                    ),
                ],
                deliverables=[
                    "카테고리 후보/속성 태그 시트",
                    "운영 가이드 템플릿 + 샘플",
                    "파이프라인 Swimlane & PoC 계획",
                ],
                success_metrics=[
                    "핵심 카테고리 6~8개 확정",
                    "워크숍 Must Fix 3건 이하",
                    "PoC 2건 phase-018 연동",
                ],
                timeline=[
                    {"day": "D1", "focus": "후보 발산 워크숍, 여정 맵 업데이트"},
                    {"day": "D2", "focus": "우선순위 매트릭스, 속성 태깅"},
                    {"day": "D3", "focus": "운영 가이드 템플릿, Swimlane"},
                    {"day": "D4", "focus": "검증 워크숍 및 피드백"},
                    {"day": "D5", "focus": "PoC 확정, phase-018 전달"},
                ],
                dependencies=["Phase 018 Revenue model exploration", "Phase 020 storytelling"],
                guardrails=self._GUARDRAILS,
            ),
            PhasePlan(
                identifier="phase-018",
                phase=18,
                title="수익 모델 스케치",
                objective=(
                    "콘텐츠 전략과 비즈니스 목표를 연결하는 수익 스트림을 비교·설계해 재무 계획과 기능 우선순위를 뒷받침한다."
                ),
                storage_path="docs/records/phase-018/",
                tasks=[
                    PhaseTask(
                        name="시장/레퍼런스 조사",
                        description="동종 서비스 수익 구조, 단가, LTV, CAC, 규제/결제/세무 제약을 조사한다.",
                        checkpoints=[
                            "비교 표 완성",
                            "법무 검토 메모",
                        ],
                    ),
                    PhaseTask(
                        name="수익 스트림 정의",
                        description="광고·구독·커뮤니티·라이선싱·데이터 API 등 Value Chain과 Lean Canvas를 작성한다.",
                        checkpoints=[
                            "세그먼트/채널/비용 구조 기입",
                            "phase-015 Value Props 매핑",
                        ],
                    ),
                    PhaseTask(
                        name="재무 시뮬레이션",
                        description="ARPU/Conversion/Churn 가정을 명시하고 12개월 전망 시트, KPI 매핑, 민감도 분석 2건을 수행한다.",
                        checkpoints=[
                            "Phase 016 KPI 트리 연결",
                            "민감도 시나리오 주석",
                        ],
                    ),
                    PhaseTask(
                        name="리스크/로드맵",
                        description="운영/규제/파트너 리스크와 MVP 실험 로드맵 2~3건을 작성해 비용·담당·다음 단계를 명확히 한다.",
                        checkpoints=[
                            "리스크 레지스터 신규 4건",
                            "phase-019 Heat Map 입력",
                        ],
                    ),
                ],
                deliverables=[
                    "수익 스트림 비교 표 & 규제 조사",
                    "Lean Canvas/Value Chain 묶음",
                    "재무 시뮬레이션 + KPI 매핑 + 리스크/로드맵",
                ],
                success_metrics=[
                    "유효 수익 스트림 3건 Canvas+KPI 완료",
                    "핵심 가정 명시 + 민감도 2건",
                    "리스크 레지스터 신규 4건 대응",
                ],
                timeline=[
                    {"day": "D1", "focus": "벤치마크/규제 조사"},
                    {"day": "D2", "focus": "수익 스트림 정의, Lean Canvas"},
                    {"day": "D3", "focus": "재무 시뮬레이션, KPI 매핑"},
                    {"day": "D4", "focus": "리스크/로드맵 문서화, 리뷰"},
                    {"day": "D5", "focus": "피드백 반영, phase-019 전달"},
                ],
                dependencies=["Phase 015 Value Proposition", "Phase 019 Risk Matrix"],
                guardrails=self._GUARDRAILS,
            ),
            PhasePlan(
                identifier="phase-019",
                phase=19,
                title="리스크 매트릭스",
                objective=(
                    "프로젝트 전반 리스크를 식별·평가·완화하기 위한 매트릭스를 정교화해 실행 단계의 예측 가능성을 높인다."
                ),
                storage_path="docs/records/phase-019/",
                tasks=[
                    PhaseTask(
                        name="리스크 인벤토리",
                        description="phase-014~018 산출물에서 리스크를 추출하고 외부/내부 요소로 분류해 중복을 제거한다.",
                        checkpoints=[
                            "고/중 리스크 5건 이상 업데이트",
                            "Jira Risk Board 동기화",
                        ],
                    ),
                    PhaseTask(
                        name="Heat Map",
                        description="가능도·영향도(1~5) 점수로 Risk Score를 계산해 Heat Map을 시각화하고 재무/법무/보안 검증을 받는다.",
                        checkpoints=[
                            "검증 메모 첨부",
                            "감사용 스냅샷 PDF 생성",
                        ],
                    ),
                    PhaseTask(
                        name="완화 전략",
                        description="상위 10개 리스크에 대한 예방·탐지·대응 액션과 오너/타임라인을 정의하고 KPI/Alert와 연결한다.",
                        checkpoints=[
                            "상위 리스크 80% 이상 KPI 연동",
                            "Cause-Effect 다이어그램 작성",
                        ],
                    ),
                    PhaseTask(
                        name="커뮤니케이션 설계",
                        description="리스크 보고 플로우와 Slack/Incident Doc 채널을 정하고 phase-020 스토리텔링에 영향 요소를 전달한다.",
                        checkpoints=[
                            "보고 SLA 정의",
                            "phase-020 인풋 메모",
                        ],
                    ),
                ],
                deliverables=[
                    "리스크 인벤토리 & Heat Map",
                    "상위 리스크 대응 플랜/오너십 매트릭스",
                    "모니터링 지표 & Alert 매핑 문서",
                ],
                success_metrics=[
                    "고/중 리스크 각각 5건 이상",
                    "Heat Map·대응 플랜 경영진 승인",
                    "상위 리스크 80% KPI/Alert 연결",
                ],
                timeline=[
                    {"day": "D1", "focus": "리스크 수집/분류"},
                    {"day": "D2", "focus": "점수 산정 워크숍, Heat Map"},
                    {"day": "D3", "focus": "대응 전략/오너십"},
                    {"day": "D4", "focus": "모니터링/커뮤니케이션 플랜"},
                    {"day": "D5", "focus": "승인 후 phase-020에 영향 요소 전달"},
                ],
                dependencies=["Phase 016 KPI Alerts", "Phase 020 storytelling inputs"],
                guardrails=self._GUARDRAILS,
            ),
            PhasePlan(
                identifier="phase-020",
                phase=20,
                title="브랜드 스토리텔링",
                objective=(
                    "사용자·파트너·내부팀 모두에게 일관된 내러티브를 전달할 메시징 패키지를 제작해 캠페인/제품 카피/미디어 키트에 즉시 활용한다."
                ),
                storage_path="docs/records/phase-020/",
                tasks=[
                    PhaseTask(
                        name="스토리 재료 수집",
                        description="phase-013~019 핵심 메시지·사용자 인용·데이터 포인트를 Story Bank로 정리하고 톤/금지어 가이드를 점검한다.",
                        checkpoints=[
                            "Story Bank 태그 체계 구축",
                            "문화적 감수성 리뷰 요청",
                        ],
                    ),
                    PhaseTask(
                        name="내러티브 아키텍처",
                        description="Hero's Journey, Problem-Insight-Solution, Before/After 프레임을 조합해 세그먼트별 Key Message+Proof+CTA 매트릭스를 만든다.",  # noqa: E501
                        checkpoints=[
                            "채널 4개 이상 커버",
                            "Risk 입력 반영",
                        ],
                    ),
                    PhaseTask(
                        name="콘텐츠 자산 초안",
                        description="브랜드 스토리 원페이저, 피치덱 3장, 온보딩 카피/FAQ, 이미지·모션 톤보드를 작성한다.",
                        checkpoints=[
                            "자산 80% 이상 템플릿화",
                            "외부 공유/내부 버전 분리",
                        ],
                    ),
                    PhaseTask(
                        name="피드백 & 롤아웃",
                        description="마케팅·제품·커뮤니티 스토리 리뷰 후 캠페인/제품 릴리스 캘린더와 연계한 롤아웃 플랜을 세운다.",
                        checkpoints=[
                            "리드 승인 및 수정 3건 이하",
                            "캘린더·책임자 명시",
                        ],
                    ),
                ],
                deliverables=[
                    "Story Bank & 내러티브 아키텍처",
                    "브랜드 스토리 원페이저/피치덱/온보딩 카피/FAQ/톤보드",
                    "롤아웃 플랜 & 채널별 메시지 매트릭스",
                ],
                success_metrics=[
                    "마케팅·제품 리드 승인, 수정 3건 이하",
                    "채널 4개 이상 메시지 매트릭스",
                    "자산 80% 이상 템플릿 제공",
                ],
                timeline=[
                    {"day": "D1", "focus": "Story Bank 수집, 톤 점검"},
                    {"day": "D2", "focus": "내러티브 아키텍처, 메시지 매트릭스"},
                    {"day": "D3", "focus": "콘텐츠 자산/톤보드 제작"},
                    {"day": "D4", "focus": "리뷰 세션, 피드백 반영"},
                    {"day": "D5", "focus": "롤아웃 플랜 확정, 후속 페이즈 핸드오프"},
                ],
                dependencies=["Phase 015 Messaging pillars", "Phase 019 Risk playbooks"],
                guardrails=self._GUARDRAILS,
            ),
        ]

    _ARCHITECTURE_SPECS = [
        {
            "phase": 21,
            "theme": "시스템 다이어그램",
            "objective_focus": "시스템 다이어그램 심화",
            "storage_path": "docs/records/phase-021/",
            "diagram_layers": "사용자 여정·서비스·데이터 저장소 3계층",
            "decision_scope": "렌더링/콘텐츠 파이프라인/번역 워커",
            "stress_area": "지연 시간과 단일 장애점",
            "poc_focus": "Graphviz/Structurizr 자동 생성 PoC",
            "validation_forum": "Architecture Sync",
            "dependencies": [
                "Phase 014 경쟁 구도 인텔리전스",
                "Phase 015 가치 제안 정교화",
            ],
        },
        {
            "phase": 22,
            "theme": "데이터 흐름",
            "objective_focus": "데이터 흐름 심화",
            "storage_path": "docs/records/phase-022/",
            "diagram_layers": "수집→정제→큐레이션→분석 흐름",
            "decision_scope": "ETL/ELT 도구, 메시지 큐, 데이터 모니터링",
            "stress_area": "데이터 지연/품질 리스크",
            "poc_focus": "CDC·스트리밍 데이터 품질 PoC",
            "validation_forum": "Data Council",
            "dependencies": [
                "Phase 017 콘텐츠 카테고리 디자인",
                "Phase 019 Risk Register",
            ],
        },
        {
            "phase": 23,
            "theme": "API 게이트웨이",
            "objective_focus": "API 게이트웨이 심화",
            "storage_path": "docs/records/phase-023/",
            "diagram_layers": "인입 채널·게이트웨이·서비스 메쉬",
            "decision_scope": "라우팅, 인증, 관찰성 컴포넌트",
            "stress_area": "스파이크 트래픽과 보안",
            "poc_focus": "레이트 리밋/제로다운 PoC",
            "validation_forum": "Platform Review",
            "dependencies": [
                "Phase 018 Revenue instrumentation",
                "Phase 020 스토리텔링 롤아웃",
            ],
        },
        {
            "phase": 24,
            "theme": "이벤트 버스",
            "objective_focus": "이벤트 버스 심화",
            "storage_path": "docs/records/phase-024/",
            "diagram_layers": "프로듀서·버스·컨슈머",
            "decision_scope": "QoS, 리플레이, 멱등성 설계",
            "stress_area": "중복 처리와 순서 보장",
            "poc_focus": "Exactly-once 전달 PoC",
            "validation_forum": "Streaming Guild",
            "dependencies": [
                "Phase 015 가치 제안 정교화",
                "Phase 022 데이터 흐름 심화",
            ],
        },
        {
            "phase": 25,
            "theme": "캐시 전략",
            "objective_focus": "캐시 전략 심화",
            "storage_path": "docs/records/phase-025/",
            "diagram_layers": "에지·애플리케이션·데이터 계층",
            "decision_scope": "TTL, 무효화 정책, 지역화",
            "stress_area": "정합성과 비용",
            "poc_focus": "멀티 레벨 캐시 성능 PoC",
            "validation_forum": "Performance Clinic",
            "dependencies": [
                "Phase 017 콘텐츠 카테고리 디자인",
                "Phase 023 API 게이트웨이 심화",
            ],
        },
        {
            "phase": 26,
            "theme": "스토리지 옵션",
            "objective_focus": "스토리지 옵션 심화",
            "storage_path": "docs/records/phase-026/",
            "diagram_layers": "OLTP·OLAP·오브젝트 스토리지",
            "decision_scope": "RPO/RTO, 복제, 암호화",
            "stress_area": "확장성과 비용 대비 안정성",
            "poc_focus": "하이브리드 스토리지 마이그레이션 PoC",
            "validation_forum": "Data Platform Review",
            "dependencies": [
                "Phase 021 시스템 다이어그램 심화",
                "Phase 022 데이터 흐름 심화",
            ],
        },
        {
            "phase": 27,
            "theme": "보안 토폴로지",
            "objective_focus": "보안 토폴로지 심화",
            "storage_path": "docs/records/phase-027/",
            "diagram_layers": "아이덴티티·비밀관리·네트워크 경계",
            "decision_scope": "IAM, 비밀 주기, 위협 탐지",
            "stress_area": "권한 상승·데이터 유출",
            "poc_focus": "제로트러스트 경로 검증 PoC",
            "validation_forum": "Security Review Board",
            "dependencies": [
                "Phase 019 Risk Register",
                "Phase 026 스토리지 옵션 심화",
            ],
        },
    ]

    def _build_architecture_plans(self) -> List[PhasePlan]:
        plans: List[PhasePlan] = []
        for spec in self._ARCHITECTURE_SPECS:
            theme = spec["theme"]
            phase = spec["phase"]
            identifier = f"phase-{phase:03d}"
            title = f"아키텍처 및 기술 스택 설계 - {theme}"
            objective = (
                "프론트엔드, 백엔드, 크롤러, 번역 파이프라인을 아우르는 기술 구조를 정의한다. "
                f"이번 페이즈는 **{spec['objective_focus']}**에 중점을 둔다."
            )

            tasks = [
                PhaseTask(
                    name=f"{theme} 요구·경계 인벤토리",
                    description=(
                        f"Phase 013~020 산출물과 이해관계자 인터뷰로 {theme} 관련 요구를 수집하고 "
                        "경계·소유권·리스크를 태깅한다."
                    ),
                    checkpoints=[
                        "요구사항 트레이스 매트릭스 100% 작성",
                        f"{spec['dependencies'][0]} 연동 조건 명시",
                    ],
                ),
                PhaseTask(
                    name=f"{theme} 블루프린트",
                    description=(
                        f"{spec['diagram_layers']}을 포함한 다이어그램을 작성하고 시각적 노테이션을 표준화한다."
                    ),
                    checkpoints=[
                        "다이어그램 3계층 이상 표현",
                        "리스크·가정 라벨링",
                    ],
                ),
                PhaseTask(
                    name="기술 대안 매트릭스",
                    description=(
                        f"{spec['decision_scope']} 후보를 비용/성능/운영성 지표로 비교하고 선택 기준을 문서화한다."
                    ),
                    checkpoints=[
                        "Scorecard에 수치/출처 기재",
                        "의사결정 로그 ADR에 연결",
                    ],
                ),
                PhaseTask(
                    name="PoC & 리뷰",
                    description=(
                        f"{spec['poc_focus']}을 실행해 {spec['stress_area']}을 검증하고 {spec['validation_forum']}에서 승인받는다."
                    ),
                    checkpoints=[
                        "PoC 측정 로그 첨부",
                        "리뷰 피드백을 Issue Tracker에 백필",
                    ],
                ),
            ]

            deliverables = [
                f"{theme} 다이어그램 & 아키텍처 데크",
                "기술 의사결정 레코드(ADR)",
                f"{spec['poc_focus']} 결과 리포트",
            ]

            success_metrics = [
                "ADR 승인 리드타임 3일 이내",
                f"{theme} 핵심 리스크 100% 대응 전략 등록",
                f"PoC에서 {spec['stress_area']} 개선 근거 확보",
            ]

            timeline = [
                {"day": "D1", "focus": f"{theme} 요구·리스크 수집"},
                {"day": "D2", "focus": f"{theme} 다이어그램/{spec['diagram_layers']} 정리"},
                {"day": "D3", "focus": f"{spec['decision_scope']} 대안 비교"},
                {"day": "D4", "focus": f"{spec['poc_focus']} 실행"},
                {"day": "D5", "focus": f"{spec['validation_forum']} 리뷰 & 핸드오프"},
            ]

            plans.append(
                PhasePlan(
                    identifier=identifier,
                    phase=phase,
                    title=title,
                    objective=objective,
                    storage_path=spec["storage_path"],
                    tasks=tasks,
                    deliverables=deliverables,
                    success_metrics=success_metrics,
                    timeline=timeline,
                    dependencies=spec["dependencies"],
                    guardrails=self._GUARDRAILS,
                )
            )
        return plans

    def list_plans(self, start: int, end: int) -> List[Dict[str, Any]]:
        key = (start, end)
        if key not in self._plans_by_range:
            raise ValueError(f"Unknown phase range: {start}-{end}")
        return [plan.to_dict() for plan in self._plans_by_range[key]]


phase_strategy_service = PhaseStrategyService()

