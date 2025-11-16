# KPI Sync Template (Phase 013 → Phase 018/019/024)

아래 템플릿은 WS-013E 산출물 공유 후 48시간 내 각 오너가 준수 여부를 회신할 때 사용하는 표준 양식이다. Issue Tracker에서 복사해 사용한다.

## Checklist
- [ ] 연결된 워크스트림 (예: WS-013E)
- [ ] 참조 의사결정 번호(DEC-051/052 등)
- [ ] 수신 페이즈/오너 (Phase 018 Data, Phase 019 Product Ops, Phase 024 Sales)
- [ ] 필요한 KPI/로그 필드 (JSON/YAML key)
- [ ] 가드레일 영향(비용/저작권/모델)
- [ ] 회신 상태 (`수용`, `조건부`, `블로커`)
- [ ] Follow-up 이슈 링크

## Example Front Matter
```yaml
issues: ["#ISS-334", "#ISS-335"]
workstream: WS-013E
guardrails:
  cost: true
  copyright: true
  model: true
sla_hours: 48
```

## 제출 규칙
1. 회신자는 Issue 코멘트와 본 템플릿 모두에 동일한 데이터를 남긴다.
2. `블로커` 상태일 경우 리스크 레지스터(RSK-051/052/053) 중 어떤 항목을 자극하는지 명시해야 한다.
3. 템플릿 파일은 `docs/records/phase-013/evidence/trust-signals/` 폴더에 저장하며, 버전 변경 시 Pull Request에 링크한다.
