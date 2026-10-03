# Deployment Guide

## Сервис

**AI-система выделения и актуализации клиентских правок из переписки дизайнера**

На ЛР1 разворачивается рабочая hello-world заглушка API. Реальная AI-логика будет добавляться в следующих лабораторных работах.

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

После запуска:

- API: http://localhost:8000
- Health check: http://localhost:8000/health
- Swagger: http://localhost:8000/docs

Остановка:

```bash
docker compose -f compose.dev.yml down
```

## Production deployment — Render

### Настройки

- Service type: `Web Service`
- Runtime / Language: `Docker`
- Branch: `lab1-delivery-initiation` до merge PR, затем `main`
- Root Directory: пусто
- Instance type: `Free`
- Health Check Path: `/health`

Docker-контейнер запускает приложение командой из `Dockerfile`.
Приложение слушает `0.0.0.0` и использует переменную окружения `PORT`, предоставляемую Render.

## Production URL

После первого успешного деплоя вставить сюда реальную ссылку:

```text
https://YOUR-SERVICE.onrender.com
```

Health check:

```text
https://YOUR-SERVICE.onrender.com/health
```

После получения ссылки необходимо также заменить `TODO` в секции `Production` файла `README.md`.

## Проверка после деплоя

Должны открываться:

1. `/` — информация о проекте и статус `ok`;
2. `/health` — статус `healthy`;
3. `/docs` — Swagger UI.

Пример проверки:

```bash
curl https://YOUR-SERVICE.onrender.com/health
```

Ожидаемый ответ:

```json
{
  "status": "healthy",
  "service": "client-edits-ai"
}
```
