FROM python:3.8-slim-buster
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry && poetry config virtualenvs.create false && poetry install
COPY main.py .

CMD [ "python3", "main.py"]