FROM python:3.12-slim
WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY artefacts artefacts
COPY backend/*.py/ .
COPY frontend frontend

RUN --mount=source=dist,target=/dist PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir /dist/*.whl

EXPOSE 5001

CMD ["python", "app.py"]
