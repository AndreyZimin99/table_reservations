#  Table_reservations

**Table_reservations** — это API-сервис бронирования столиков в ресторане.

## Используемый стек:
   - Python;
   - FastAPI;
   - SQLAlchemy;
   - Alembic;
   - Docker;
   - Gunicorn

## Установка

Чтобы развернуть проект на локальной машине, выполните следующие команды в терминале:

1. **Клонируйте репозиторий:**
   ```
   git clone https://github.com/AndreyZimin99/table_reservations.git
   ```
   ```
   cd table_reservations
   ```

2. **Запустите проект:**
   ```
   docker-compose up -d
   ```

3. **Выполните миграции:**
   ```
   docker-compose exec app alembic upgrade head 
   ```

## Документация:
   ```
   http://127.0.0.1:8000/docs
   ```

## Пример заполнения файла  .env:
   ```
   POSTGRES_DB=postgres
   POSTGRES_USER=postgres_user
   POSTGRES_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   ```
   
@@@AndreyZimin99@@@
