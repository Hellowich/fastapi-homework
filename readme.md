# Инструкция по запуску проекта

## Установка и запуск

1. Клонируйте репозиторий:
    ```sh
    git clone <URL вашего репозитория>
    ```
2. Перейдите в директорию проекта:
    ```sh
    cd fastapi_homework
    ```
3. Создайте и активируйте виртуальное окружение:
    ```sh
    python -m venv venv
    source venv/bin/activate   # Для Linux/macOS
    venv\\Scripts\\activate    # Для Windows
    ```
4. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```
5. Запустите сервер:
    ```sh
    uvicorn main:app --reload
    ```

## Для Docker
### Через Билд
1. Переходим к директории с dockerfile
   ```sh
   cd fastapi_homework
   ```
2. Билдим образ
   ```sh
   docker build -t fastapi-homework .
   ```
3. Запускаем образ
   ```sh
   docker run -d -p 8000:8000 fastapi-homework
   ```

### Из образа
1. Клонируйте образ из репозитория
    ```sh
     docker pull fobosyatina/techorda-homework-sailaukhan:latest
    ```
3. Запустите контейнер
    ```sh
    docker run -d -p 8000:8000 --name techorda_app fobosyatina/techorda-homework-sailaukhan:latest
    ```
## Тестирование

Для тестирования всех эндпоинтов используется Postman. Экспортированная коллекция находится в проекте.
