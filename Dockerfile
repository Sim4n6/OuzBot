FROM python:3.7.4

LABEL Author="ALJI Mohamed"
LABEL E-mail="sim4n6@gmail.com"
LABEL version="0.0.2"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "Stats-Bot.py"

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0