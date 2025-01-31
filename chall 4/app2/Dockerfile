FROM python:3.9-alpine
WORKDIR /app
COPY Hello.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
CMD [ "flask", "--app", "Hello", "run","--host=0.0.0.0" ]