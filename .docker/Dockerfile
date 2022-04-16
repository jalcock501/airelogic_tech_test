# Docker template to generate working CLI
FROM python:slim

RUN useradd --create-home --shell /bin/bash app_user

RUN pip install poetry

WORKDIR /home/app_user

ADD ./poetry.lock .
ADD ./pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install

USER app_user

ADD --chown=app_user:app_user airelogic_tech_test ./airelogic_tech_test

CMD ["bash"] 