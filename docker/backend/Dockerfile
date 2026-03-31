FROM python:3.11-slim

WORKDIR /app

# Copia requirements e instala dependências
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia código do backend
COPY backend/app ./app

# Copia ontologia
COPY ontology /ontology

CMD ["uvicorn", "app.ml.main:app", "--host", "0.0.0.0", "--port", "8001"]
