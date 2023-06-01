FROM python:3.10-slim-buster
RUN apt-get -y update && apt-get install -y ffmpeg libsm6 libxext6
RUN pip install poetry
WORKDIR opt/stoloto
COPY . .
RUN poetry config virtualenvs.create false && poetry install
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--timeout-keep-alive", "60", "--log-level", "info"]
