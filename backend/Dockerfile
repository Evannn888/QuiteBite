FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

CMD ["python", "run.py"] 