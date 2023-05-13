# pull official base image
FROM python:3.6-alpine
LABEL maintainer="evalladarestav@gmail.com"
ENV PYTHONUNBUFFERED=1
ENV PYCURL_SSL_LIBRARY=openssl
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python3 -m pip install --upgrade pip
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]