# Discord 알림 설정 가이드

GitHub에서 main 브랜치에 merge가 발생했을 때 Discord로 알림을 받을 수 있습니다.

## 1. Discord 웹훅 생성

### 단계별 설정

1. **Discord 서버 설정 열기**
   - 알림을 받을 Discord 채널에서 톱니바퀴 아이콘 클릭
   - "채널 편집" 선택

2. **웹훅 생성**
   - 왼쪽 메뉴에서 "연동" 또는 "Integrations" 선택
   - "웹훅" 또는 "Webhooks" 클릭
   - "새 웹훅" 또는 "New Webhook" 버튼 클릭

3. **웹훅 설정**
   - 이름: `Intern App Bot` (원하는 이름으로 변경 가능)
   - 채널: 알림을 받을 채널 선택
   - "웹훅 URL 복사" 버튼 클릭하여 URL 복사

   웹훅 URL 형식:
   ```
   https://discord.com/api/webhooks/[WEBHOOK_ID]/[WEBHOOK_TOKEN]
   ```

## 2. GitHub Secrets 설정

1. **GitHub 저장소로 이동**
   - 저장소 페이지에서 `Settings` 탭 클릭

2. **Secrets 추가**
   - 왼쪽 메뉴에서 `Secrets and variables` > `Actions` 선택
   - `New repository secret` 버튼 클릭

3. **Secret 생성**
   - Name: `DISCORD_WEBHOOK`
   - Value: 복사한 Discord 웹훅 URL 붙여넣기
   - `Add secret` 버튼 클릭

## 3. 워크플로우 선택

두 가지 버전의 알림 워크플로우가 제공됩니다:

### 옵션 1: 간단한 버전 (추천)
- **파일**: `.github/workflows/discord-notification.yml`
- **특징**:
  - 간결한 알림
  - 커밋 메시지, 작성자, 링크 포함
  - 설정 및 유지보수 쉬움

### 옵션 2: 상세한 버전
- **파일**: `.github/workflows/discord-notification-detailed.yml`
- **특징**:
  - 상세한 정보 포함
  - 변경된 파일 목록 표시
  - 커스터마이징 가능한 임베드 메시지

**둘 중 하나만 사용**하려면 나머지 파일을 삭제하세요:
```bash
# 상세 버전만 사용하려면
rm .github/workflows/discord-notification.yml

# 또는 간단한 버전만 사용하려면
rm .github/workflows/discord-notification-detailed.yml
```

## 4. 알림 테스트

1. **main 브랜치에 변경사항 push**
   ```bash
   git add .
   git commit -m "test: Discord 알림 테스트"
   git push origin main
   ```

2. **또는 PR을 main에 merge**
   - PR 생성 후 merge
   - 자동으로 Discord에 알림 전송

## 5. 알림 예시

### 간단한 버전
```
✅ Main 브랜치에 새로운 변경사항이 병합되었습니다!

커밋 메시지: feat: 새로운 기능 추가
작성자: your-username
브랜치: main

[커밋 보기](링크)
```

### 상세한 버전
```
✅ Main 브랜치에 병합되었습니다
feat: 새로운 기능 추가

👤 작성자: your-username
📝 타입: PR
🌿 브랜치: main
📂 변경된 파일: backend/app/main.py, frontend/src/app.ts, ...
🔗 링크: [변경사항 보기](링크)
```

## 6. 커스터마이징

### 알림 색상 변경
`discord-notification.yml` 파일에서:
```yaml
color: 0x00ff00  # 녹색 (성공)
# 다른 색상 예시:
# 0xff0000  # 빨간색
# 0x0000ff  # 파란색
# 0xffff00  # 노란색
```

### 봇 이름 및 아바타 변경
```yaml
username: "Intern App Bot"  # 원하는 이름으로 변경
avatar_url: "이미지_URL"     # 원하는 아바타 URL로 변경
```

### 특정 조건에만 알림 보내기
```yaml
# 예: 특정 파일이 변경된 경우에만
on:
  push:
    branches:
      - main
    paths:
      - 'backend/**'
      - 'frontend/**'
```

## 문제 해결

### 알림이 오지 않는 경우
1. GitHub Secrets에 `DISCORD_WEBHOOK`이 제대로 설정되었는지 확인
2. 웹훅 URL이 유효한지 확인
3. GitHub Actions 탭에서 워크플로우 실행 로그 확인
4. Discord 채널 권한 확인

### 웹훅 URL 테스트
터미널에서 직접 테스트:
```bash
curl -H "Content-Type: application/json" \
     -d '{"content": "테스트 메시지"}' \
     "YOUR_DISCORD_WEBHOOK_URL"
```

## 추가 설정

### 여러 채널에 알림 보내기
각 채널마다 웹훅을 생성하고 여러 개의 Secret을 추가:
- `DISCORD_WEBHOOK_GENERAL`
- `DISCORD_WEBHOOK_DEV`
- `DISCORD_WEBHOOK_ALERTS`

그리고 워크플로우에서 각각 호출하세요.

### CI 실패 시 알림
별도의 워크플로우를 만들어 CI 실패 시에도 알림을 받을 수 있습니다.
