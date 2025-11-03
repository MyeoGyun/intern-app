# Intern App

AI를 위한 수학 공부에 입문하려는 유저들을 대상으로 체계적인 수학 커리큘럼과 퀴즈문제를 통해 기초 학습에 도움을 제공하는 앱

## 프로젝트 구조

```
intern-app/
├── backend/              # FastAPI 백엔드
│   ├── app/
│   │   ├── api/         # API 엔드포인트 및 라우터
│   │   ├── core/        # 핵심 설정 및 유틸리티
│   │   ├── models/      # 데이터베이스 모델 (ORM)
│   │   ├── schemas/     # Pydantic 스키마
│   │   ├── services/    # 비즈니스 로직
│   │   └── main.py      # FastAPI 앱 엔트리포인트
│   ├── tests/           # 백엔드 테스트
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/            # NestJS 프론트엔드
│   ├── src/
│   │   ├── modules/    # NestJS 모듈
│   │   ├── common/     # 공통 코드 (인터셉터, 가드 등)
│   │   ├── config/     # 설정 파일
│   │   ├── main.ts     # NestJS 앱 엔트리포인트
│   │   └── app.module.ts
│   ├── test/           # E2E 테스트
│   ├── package.json
│   └── Dockerfile
│
├── .github/
│   └── workflows/      # CI/CD 워크플로우
└── docker-compose.yml  # Docker Compose 설정
```

## 기술 스택

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.10+
- **ORM**: SQLAlchemy
- **Testing**: Pytest
- **Linting**: Ruff, Black
- **Type Checking**: MyPy

### Frontend
- **Framework**: NestJS
- **Language**: TypeScript
- **Testing**: Jest
- **Linting**: ESLint
- **Formatting**: Prettier

## 시작하기

### 사전 요구사항
- Python 3.10 이상
- Node.js 18 이상
- Docker & Docker Compose (선택사항)

### Backend 설정

```bash
cd backend

# 가상 환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements-dev.txt

# 환경 변수 설정
cp .env.example .env

# 개발 서버 실행
uvicorn app.main:app --reload
```

Backend 서버: http://localhost:8000
API 문서: http://localhost:8000/docs

### Frontend 설정

```bash
cd frontend

# 의존성 설치
npm install

# 환경 변수 설정
cp .env.example .env

# 개발 서버 실행
npm run start:dev
```

Frontend 서버: http://localhost:3000

### Docker로 실행

```bash
# 전체 스택 실행
docker-compose up -d

# 로그 확인
docker-compose logs -f

# 중지
docker-compose down
```

## 개발 가이드

### Backend 테스트

```bash
cd backend

# 테스트 실행
pytest

# 커버리지와 함께 테스트
pytest --cov=app

# 린트 검사
ruff check .

# 포맷 체크
black --check .

# 타입 체크
mypy .
```

### Frontend 테스트

```bash
cd frontend

# 단위 테스트
npm run test

# 커버리지와 함께 테스트
npm run test:cov

# E2E 테스트
npm run test:e2e

# 린트 검사
npm run lint

# 타입 체크
npm run type-check

# 빌드
npm run build
```

## CI/CD

GitHub Actions를 통해 자동으로 다음 작업이 실행됩니다:

- **Backend CI**: 린트, 타입 체크, 테스트 (Python 3.10, 3.11, 3.12)
- **Frontend CI**: 린트, 타입 체크, 테스트, 빌드 (Node.js 18, 20)
- **Full Stack CI**: 백엔드와 프론트엔드 통합 테스트

## 기여하기

프로젝트 기여 방법은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고해주세요.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE)를 참고해주세요.
