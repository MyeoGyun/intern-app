FROM node:20-alpine AS builder

WORKDIR /app

# 의존성 설치
COPY package*.json ./
RUN npm ci

# 애플리케이션 코드 복사 및 빌드
COPY . .
RUN npm run build

# Production 이미지
FROM node:20-alpine

WORKDIR /app

# 프로덕션 의존성만 설치
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# 빌드된 파일 복사
COPY --from=builder /app/dist ./dist

# 포트 노출
EXPOSE 3000

# 애플리케이션 실행
CMD ["node", "dist/main"]
