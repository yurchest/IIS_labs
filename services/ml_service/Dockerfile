FROM python:3.12-slim

# Скопировать содержимое текущей директории в директорию /ml_service в контейнере
COPY . /ml_service

# Сделать директорию /models доступной снаружи контейнера
VOLUME /models

# Сделать /ml_service рабочей директорией
WORKDIR /ml_service

# Выполнить установку всех зависимостей из файла requirements.txt
RUN pip install -r requirements.txt

# Указать, что порт 8000 должен быть доступен снаружи контейнера
EXPOSE 8000

# Финальная команда - запуск сервера. Необходимо явно указать адрес хоста "0.0.0.0" и порта "8000", на которых будет запускаться сервер.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

# docker build . --tag score_model:1
# docker run -p 8001:8000 -v $(pwd)/../models:/models score_model:1