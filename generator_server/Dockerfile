FROM python:3

WORKDIR /webserver/
ENV FLASK_APP=webserver.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

COPY ./webserver.py .
COPY ./passwordGeneratorApp.out .
COPY ./.env .
CMD [ "flask", "run", "--cert=adhoc"]
