FROM python:3.11-slim

COPY main.py /main.py
ENTRYPOINT ["python", "/main.py"]
