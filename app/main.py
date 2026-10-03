from fastapi import FastAPI
from pydantic import BaseModel


PROJECT_NAME = "AI-система выделения и актуализации клиентских правок из переписки дизайнера"

app = FastAPI(
    title=PROJECT_NAME,
    description=(
        "Учебная заглушка проекта для ЛР1. "
        "Система предназначена для выделения клиентских правок из переписки "
        "и подготовки их к последующей актуализации."
    ),
    version="0.1.0",
)


class DemoMessage(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "status": "ok",
        "project": PROJECT_NAME,
        "message": "Hello-world: сервис запущен и готов к дальнейшей разработке.",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "client-edits-ai",
    }


@app.post("/api/v1/demo")
def demo(payload: DemoMessage):
    """
    Демонстрационная заглушка ЛР1.
    Реальное AI-выделение правок будет реализовано в следующих лабораторных.
    """
    return {
        "status": "stub",
        "source_text": payload.text,
        "extracted_edits": [],
        "message": "AI-обработка пока не подключена: это hello-world заглушка ЛР1.",
    }
