# 1 
FROM python:3.6

RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove


# 2
COPY . /app

WORKDIR /app

#3

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 manage.py
RUN chmod 444 requirements.txt

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT Detection.wsgi --timeout 900