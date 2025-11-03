### Contributing 정의서
1) 브랜치 전략
- 기본 브랜치: dev (기본 작업/통합)
- 배포 브랜치: main (태그 기준 배포)
- 작업 브랜치: feat/*, fix/*, chore/*, docs/*, refactor/*, test/*
- 머지 방식: PR 필수
    - .github/pull_request_template.md

2) 커밋 메시지 규칙
- type: feat, fix, docs, style, refactor, test, chore, build, ci
- scope: 선택(모듈/패키지명 등). 예: api, db, ui
- subject: 50자 내, 한글/영문 가능, 끝에 마침표 X
- body: 변경 이유/배경, 주요 변경점 bullet
- footer: 이슈 참조 Closes #123

예시:
```
feat(api): 사용자 인증 토큰 재발급 로직 추가

- refresh grant 대응
- 만료 임박 토큰 자동 갱신

Closes #42
```
3) PR 규칙
- PR 템플릿 사용
- 라벨: feat, fix, docs, breaking 등
- CI 체크 통과 필수 (lint, test, type-check)