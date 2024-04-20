FROM python:3.10.8-buster

WORKDIR /opt/profile-mananger-service

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip && \
    pip install "poetry==1.6.1" && \
    poetry config virtualenvs.create false && \
    poetry install

COPY src src
COPY scripts scripts
COPY tests tests
COPY alembic.ini ./
COPY alembic alembic

ENV PYTHONPATH /opt/profile-mananger-service

CMD ["python", "src/bin/api.py"]