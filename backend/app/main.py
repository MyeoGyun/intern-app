from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Welcome to Intern App API", "version": settings.VERSION}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# API 라우터 등록 (추후 추가)
# from app.api.v1.api import api_router
# app.include_router(api_router, prefix=settings.API_V1_STR)
