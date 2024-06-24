FROM python:3.10-slim

ARG PACKAGE_VERSION
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/src/

COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt
RUN pip install visby==$PACKAGE_VERSION

CMD uvicorn visby.main:app --host 0.0.0.0 --port 8000