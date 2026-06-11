FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml ./
COPY toolbot ./toolbot

RUN pip install --no-cache-dir -e .

EXPOSE 5000

CMD ["flask", "--app", "toolbot:create_app", "run", "--host=0.0.0.0", "--port=5000"]
