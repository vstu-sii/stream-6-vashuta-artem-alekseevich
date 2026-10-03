from fastapi import FastAPI
from pydantic import BaseModel, Field


PROJECT_NAME = "AI-система выделения и актуализации клиентских правок из переписки дизайнера"
SERVICE_NAME = "designer-client-edits-ai"
VERSION = "0.1.0"


app = FastAPI(
    title=PROJECT_NAME,
    description=(
        "Учебный API проекта. На этапе ЛР1 реализована инфраструктурная "
        "заглушка без подключения LLM и реальной AI-обработки."
    ),
    version=VERSION,
)


class DemoRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Фрагмент переписки дизайнера с клиентом",
        examples=["Сделайте логотип меньше и замените цвет кнопки."],
    )


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "project": PROJECT_NAME,
        "version": VERSION,
        "message": "Сервис запущен и готов к дальнейшей разработке.",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": SERVICE_NAME,
        "version": VERSION,
    }


@app.post("/api/v1/demo")
def demo(payload: DemoRequest):
    """
    Демонстрационная заглушка ЛР1.

    Реальное выделение и актуализация клиентских правок
    будут реализованы на следующих этапах проекта.
    """
    return {
        "status": "stub",
        "source_text": payload.text,
        "extracted_edits": [],
        "message": (
            "AI-обработка пока не подключена. "
            "Endpoint демонстрирует будущую точку интеграции."
        ),
    }
