# FROM python:latest
# WORKDIR /app
# COPY requirements.txt /app
# RUN pip install -r requirements.txt   # package # cache # temperary
# COPY main.py /app
# EXPOSE 5000
# CMD ["python", "main.py"]

## Builder stage
FROM python:3.14-slim AS builder
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

## Runtime stage 
FROM python:3.14-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY main.py /app
EXPOSE 5000
CMD ["python", "main.py"]