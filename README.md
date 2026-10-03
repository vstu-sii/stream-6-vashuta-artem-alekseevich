# AI-система выделения и актуализации клиентских правок из переписки дизайнера

Учебный проект по дисциплине «Системы искусственного интеллекта».

## Описание проекта

### Проблема

В процессе работы дизайнер получает клиентские правки в мессенджерах и других каналах переписки. Правки могут повторяться, уточняться, отменяться или противоречить предыдущим сообщениям, из-за чего актуальное состояние требований приходится поддерживать вручную.

### Решение

Проект представляет собой AI-систему для анализа переписки дизайнера с клиентом. Система должна выделять отдельные клиентские правки, связывать их с предыдущими требованиями и поддерживать актуальное состояние списка правок с учётом уточнений, отмен и изменений.

Например, если клиент сначала просит уменьшить логотип, а затем пишет, что размер нужно оставить прежним, первая правка должна считаться неактуальной.

В ЛР1 реализована инфраструктурная основа проекта: FastAPI-приложение, Docker-окружение, автоматические тесты, CI и возможность публичного развёртывания.

### Целевая аудитория

- дизайнеры;
- дизайн-команды;
- менеджеры дизайн-проектов;
- специалисты, которые получают большое количество итеративных правок от клиентов.

### Пример

Исходная переписка:

> Клиент: Сделайте логотип меньше.  
> Клиент: Нет, размер логотипа оставьте как был. Лучше увеличьте отступ сверху.

Ожидаемое актуальное состояние правок:

- размер логотипа — без изменений;
- увеличить верхний отступ.

## Команда

| Роль | Участник | Основные задачи |
|---|---|---|
| Product / Vision Owner | Мамаев Николай Федорович, САПР-2.3 | Сегмент, гипотезы, use cases, скоуп |
| AI Engineer | Иванов Александр Викторович, САПР-2.3 | AI-подход, модели, промпты, качество |
| Delivery Engineer | Меньшенин Максим Сергеевич, САПР-2.3 | Приложение, Docker Compose, CI/CD, прод |
| AI Quality & Safety Engineer | Вашута Артем Алексеевич, ЭВМ-2.3 | Evals, критерии качества, безопасность |

## Текущая архитектура ЛР1

```text
Клиент / браузер
       |
       v
   FastAPI API
       |
       +---- GET /health
       |
       +---- POST /api/v1/demo
                |
                v
         AI-заглушка (без LLM)
```

AI-модель и хранение актуального состояния правок будут добавляться на следующих этапах проекта.

## Технологический стек

- Python 3.12
- FastAPI
- Uvicorn
- Pytest
- Docker
- Docker Compose
- GitHub Actions
- Render для публичного развёртывания приложения

## Структура репозитория

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── docs/
│   └── deploy.md
├── tests/
│   └── test_app.py
├── .dockerignore
├── .env.example
├── .gitignore
├── compose.dev.yml
├── Dockerfile
├── pytest.ini
├── render.yaml
├── requirements.txt
└── README.md
```

## Локальный запуск

### Требования

Необходимо установить:

- Git
- Docker Desktop / Docker Engine
- Docker Compose

Python 3.12 требуется только для локального запуска тестов вне Docker.

### 1. Клонировать репозиторий

```bash
git clone https://github.com/vstu-sii/stream-6-vashuta-artem-alekseevich.git
cd stream-6-vashuta-artem-alekseevich
```

### 2. Создать `.env`

Linux/macOS:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 3. Запустить приложение

```bash
docker compose -f compose.dev.yml up --build
```

После запуска доступны:

- API: http://localhost:8000
- Health check: http://localhost:8000/health
- Swagger: http://localhost:8000/docs

### 4. Остановить приложение

```bash
docker compose -f compose.dev.yml down
```

## API-заглушка

### Проверка сервиса

```http
GET /health
```

Ожидаемый ответ:

```json
{
  "status": "healthy",
  "service": "designer-client-edits-ai",
  "version": "0.1.0"
}
```

### Демонстрационная точка входа

```http
POST /api/v1/demo
Content-Type: application/json

{
  "text": "Сделайте логотип меньше и замените цвет кнопки."
}
```

На ЛР1 endpoint возвращает заглушку. Он показывает место будущей AI-обработки, но не имитирует готовый AI-функционал.

## Тесты

При установленном Python 3.12:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

Тесты также автоматически запускаются в GitHub Actions.

## CI

Workflow находится в:

```text
.github/workflows/ci.yml
```

При `push` в `main` / `lab1-*` и при Pull Request в `main` выполняются:

1. установка зависимостей;
2. запуск тестов через `pytest`;
3. сборка Docker image.

Перед сдачей оба CI job должны быть зелёными.

## Production

Production URL:

```text
TODO — вставить ссылку Render после деплоя
```

Health check:

```text
TODO — вставить ссылку Render + /health
```

После деплоя необходимо заменить оба `TODO` на реальные публичные ссылки.

## Документация

- [Deployment Guide](docs/deploy.md)
- Swagger после запуска: `/docs`

## ЛР1 — Delivery

Артефакты Delivery:

- каркас репозитория и README;
- `compose.dev.yml` и `.env.example`;
- CI в `.github/workflows/ci.yml`;
- `docs/deploy.md`;
- публичный production URL в README.

Ветка для сдачи:

```text
lab1-delivery-initiation
```

Название Pull Request:

```text
Lab1: Delivery — Initiation Deliverables
```
