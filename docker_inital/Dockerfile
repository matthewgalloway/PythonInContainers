FROM python:3

WORKDIR /myproject

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_DEBUG = TRUE

CMD python flask-hello.py