# Infra

Terraform, Docker, GitHub Actions 템플릿을 통해 저비용 환경을 구성합니다. 현재 디렉터리는 아래 역할을 가집니다.

- `terraform/` – AWS Lightsail 또는 GCP Compute 인스턴스를 관리하는 IaC 템플릿.
- `modules/` – 반복 사용하는 네트워크/관측 모듈을 저장 (향후 추가).
- `deploy/` – CI에서 참조할 스크립트/매니페스트 (향후 추가).

초기화 예시:
```bash
cd infra/terraform
terraform init
terraform plan -var-file=env/dev.tfvars
```
