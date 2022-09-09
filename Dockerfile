FROM python:3.9.10


WORKDIR /.

COPY . .

RUN pip install uvicorn fastapi

# EXPOSE 8000