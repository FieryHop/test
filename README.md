# CRM Integration Project

Мини-сервис на Django для импорта и выдачи данных товаров с использованием Celery и Redis.

---

## Описание

Проект реализует:

- Импорт товаров из CSV (локального файла или по URL) в PostgreSQL через Celery таски.
- REST API для получения списка товаров с фильтрами по категории, цене и поиском по имени.
- REST API для статистики: средняя цена по категориям с кешированием.
- Асинхронную обработку задач через Celery + Redis.
- Docker Compose для удобного запуска всех сервисов (web, db, redis, celery).

---

## Быстрый старт

### Предварительные требования

- Docker и Docker Compose
- Git (опционально)

### Запуск проекта

1. Клонируйте репозиторий (если ещё не сделали)

git clone <repository-url>
cd <project-folder>
2. Подготовьте локальный CSV файл с товарами в `./data/test.csv` (пример есть в проекте), который монтируется в контейнер `/app/data/test.csv`.

3. Запустите контейнеры через Docker Compose:
docker compose up --build

4. Миграции применятся автоматически, веб-сервер будет доступен по адресу:  
`http://localhost:8000/`

5. Вызовите импорт товаров вручную (опционально) из контейнера web:

docker compose exec web python manage.py shell

from items.tasks import import_items
import_items()

---

## REST API

- Получение списка товаров с фильтрацией и поиском

GET /api/items/?category=Food&price_min=10&price_max=100&search=apple
- Получение средней цены по категориям (кешировано на 5 минут)

GET /api/stats/avg-price-by-category/


---

## Тестирование

Запустите тесты внутри контейнера web:

docker compose exec web pytest


---

## Технологии

- Python 3.11, Django 5.x, Django REST Framework  
- Celery 5.x + Redis  
- PostgreSQL 15  
- Docker + Docker Compose

---

## Структура файлов

- `items/models.py` — модели товаров  
- `items/tasks.py` — задачи импорта  
- `items/views.py` — API представления  
- `items/filters.py` — фильтры для поиска и фильтрации  
- `data/test.csv` — пример файла с товарами  
- `docker-compose.yml` — конфигурация сервисов

---

## Важные моменты
Не забудьте проверить и настроить `.env` с параметрами БД, Redis и секретным ключом Django.  

- DEBUG=True
- SECRET_KEY=
- DATABASE_URL=
- REDIS_URL=
- CELERY_BROKER_URL=redis://redis:6379/0
- CELERY_RESULT_BACKEND=redis://redis:6379/0
- DB_HOST=
- POSTGRES_DB=
- POSTGRES_USER=
- POSTGRES_PASSWORD=
- DJANGO_SETTINGS_MODULE=app.settings

Не забудьте проверить и настроить `docker-compose` с параметрами БД.  

---



