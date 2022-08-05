FROM python:3.8-slim-buster
COPY requirements.txt .
RUN pip install requirements.txt
COPY main.py .

CMD [ "python3", "main.py"]