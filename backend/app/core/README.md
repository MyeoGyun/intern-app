# Core

애플리케이션의 핵심 설정 및 유틸리티를 관리하는 디렉토리입니다.

## 역할
- 환경 설정 관리 (config.py)
- 데이터베이스 연결 관리 (database.py)
- 보안 관련 유틸리티
- 공통 의존성 관리

## 파일 설명

### config.py
- 환경 변수 및 설정 관리
- Pydantic Settings 기반 설정

### database.py
- PostgreSQL 비동기 연결 설정
- SQLAlchemy AsyncEngine 및 Session 관리
- 데이터베이스 의존성 함수
