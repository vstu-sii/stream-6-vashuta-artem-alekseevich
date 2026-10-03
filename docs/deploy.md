# Deployment Guide

## Сервис

**AI-система выделения и актуализации клиентских правок из переписки дизайнера**

В ЛР1 разворачивается рабочая инфраструктурная заглушка API. Реальная AI-логика и LLM-интеграция будут добавляться на следующих этапах проекта.

## Локальный запуск

### 1. Создать `.env`

Linux/macOS:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 2. Запустить сервис

```bash
docker compose -f compose.dev.yml up --build
```

После запуска доступны:

- API: http://localhost:8000
- Health check: http://localhost:8000/health
- Swagger: http://localhost:8000/docs

Остановка:

```bash
docker compose -f compose.dev.yml down
```

## Production deployment — Render

Для публичного развёртывания используется Render Web Service.

Рекомендуемые настройки:

- Service type: `Web Service`
- Runtime / Language: `Docker`
- Branch до merge PR: `lab1-delivery-initiation`
- Branch после merge PR: `main`
- Root Directory: оставить пустым
- Instance type: `Free`
- Health Check Path: `/health`

Приложение запускается командой из `Dockerfile`, слушает `0.0.0.0` и использует переменную окружения `PORT`, которую предоставляет Render.

## Production URL

После успешного деплоя заменить значения ниже на реальные:

```text
https://YOUR-SERVICE.onrender.com
```

Health check:

```text
https://YOUR-SERVICE.onrender.com/health
```

## Проверка после деплоя

Должны открываться:

1. `/` — информация о проекте;
2. `/health` — статус `healthy`;
3. `/docs` — Swagger UI.

Пример:

```bash
curl https://YOUR-SERVICE.onrender.com/health
```

Ожидаемый ответ:

```json
{
  "status": "healthy",
  "service": "designer-client-edits-ai",
  "version": "0.1.0"
}
```

После получения production URL его необходимо добавить также в `README.md`.
