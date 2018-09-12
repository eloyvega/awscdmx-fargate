FROM python:3.6-alpine

EXPOSE 80

ENV APP_HOME /opt/app

ADD app.tar $APP_HOME

WORKDIR $APP_HOME

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "--access-logfile", "-", "-w", "2", "-b", "0.0.0.0:80", "app:app"]
