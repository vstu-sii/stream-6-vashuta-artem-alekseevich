# AI-система выделения и актуализации клиентских правок из переписки дизайнера

[![CI](https://github.com/vstu-sii/stream-6-vashuta-artem-alekseevich/actions/workflows/ci.yml/badge.svg)](https://github.com/vstu-sii/stream-6-vashuta-artem-alekseevich/actions/workflows/ci.yml)

Учебный проект по дисциплине «Системы искусственного интеллекта».

## Описание проекта

### Проблема

В процессе работы дизайнер получает клиентские правки в мессенджерах и других каналах переписки. Правки могут повторяться, уточняться, отменяться или противоречить предыдущим сообщениям, из-за чего актуальное состояние требований приходится поддерживать вручную.

### Решение

Проект представляет собой AI-систему для анализа переписки дизайнера с клиентом. Система должна выделять отдельные клиентские правки, связывать их с предыдущими требованиями и поддерживать актуальное состояние списка правок с учётом уточнений, отмен и изменений.

Например, если клиент сначала просит уменьшить логотип, а затем пишет, что размер нужно оставить прежним, первая правка должна считаться неактуальной.

В ЛР1 реализуется инфраструктурная основа проекта: каркас репозитория, FastAPI-приложение-заглушка, Docker-окружение, автоматические проверки CI и публичное развёртывание.

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
| Delivery Engineer | Меньшенин Максим Сергеевич, САПР-2.3 | Репозиторий, dev-окружение, CI/CD, прод |
| AI Quality & Safety Engineer | Вашута Артем Алексеевич, ЭВМ-2.3 | Evals, критерии качества, безопасность |

## Структура репозитория

```text
.
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── pull_request_template.md
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
├── pyproject.toml
├── pytest.ini
├── render.yaml
├── requirements-dev.txt
├── requirements.txt
└── README.md
```

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
- Ruff
- Docker
- Docker Compose
- GitHub Actions
- Render для публичного развёртывания приложения

## Локальный запуск

### Требования

Необходимо установить:

- Git
- Docker Desktop / Docker Engine
- Docker Compose

Python 3.12 требуется только для локального запуска тестов и CI-проверок вне Docker.

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

## Правила работы с Git

### Основная ветка

Ветка `main` содержит интегрированное состояние проекта. Изменения для лабораторных работ вносятся через отдельные ветки и Pull Request.

Не рекомендуется вносить рабочие изменения непосредственно в `main`.

### Ветки ЛР1

Для каждой роли используется отдельная ветка по шаблону:

```text
lab1-[role]-initiation
```

Примеры:

```text
lab1-product-initiation
lab1-ai-initiation
lab1-delivery-initiation
lab1-quality-initiation
```

### Pull Request

Изменения из ролевой ветки отправляются в `main` через Pull Request.

Название Pull Request для ЛР1:

```text
Lab1: [Role] — Initiation Deliverables
```

Для Delivery:

```text
Lab1: Delivery — Initiation Deliverables
```

При создании Pull Request автоматически подставляется шаблон из:

```text
.github/pull_request_template.md
```

Перед merge необходимо:

1. убедиться, что изменения относятся к своей роли;
2. проверить актуальность документации;
3. убедиться, что локальный запуск работает;
4. дождаться успешного прохождения CI;
5. не добавлять в Git секреты и локальный файл `.env`.

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

## Локальные проверки

Установить зависимости для разработки:

```bash
python -m pip install -r requirements-dev.txt
```

Проверить стиль кода:

```bash
python -m ruff check app tests
```

Проверить форматирование:

```bash
python -m ruff format --check app tests
```

Запустить тесты:

```bash
python -m pytest -v
```

## CI

Workflow расположен в:

```text
.github/workflows/ci.yml
```

При `push` в `main` / `lab1-*` и при Pull Request в `main` выполняются четыре проверки:

1. **Lint** — `ruff check`;
2. **Format** — `ruff format --check`;
3. **Tests** — `pytest`;
4. **Build** — сборка Docker image.

Статус workflow отображается бейджем в начале README.

Перед merge все обязательные CI checks должны успешно завершиться.

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
