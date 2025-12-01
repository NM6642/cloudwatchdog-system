FROM python:3.11-slim

WORKDIR /app

COPY webhook.py .
COPY fix_issue.sh .

RUN pip install flask

RUN chmod +x fix_issue.sh

EXPOSE 5001

CMD ["python", "webhook.py"]
