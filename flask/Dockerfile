FROM python:3.12.4-alpine

WORKDIR /flask

COPY requirements.txt . 

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "gunicorn" ,"--timeout", "120", "--bind", "0.0.0.0:5000","wsgi:app"]