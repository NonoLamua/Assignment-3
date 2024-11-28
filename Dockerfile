# Development Stage
FROM python:3.9-slim as development
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

# Production Stage
FROM python:3.9-slim as production
WORKDIR /app
COPY --from=development /app /app
CMD ["python", "app.py"]

