FROM python:3.10-alpine
WORKDIR /code
ENV DJANGOAPP=app.py
ENV DJANGO_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .


