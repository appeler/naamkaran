FROM python:3.11-slim

COPY ./requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
	pip install -r requirements.txt
RUN pip install gradio

ENV PYTHONUNBUFFERED 1

COPY . .

CMD ["python", "gradio_app.py"]
