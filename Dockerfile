FROM python:3.10-slim

WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV FLASK_APP=wake_on_lan.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8081

EXPOSE 8081

CMD ["flask", "run"]
