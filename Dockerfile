FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app app
COPY run.sh run.sh

COPY . .

RUN chmod +x run.sh

CMD ["sh", "run.sh"]


