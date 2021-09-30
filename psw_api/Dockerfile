FROM alpine:3.14

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python 
RUN python3 -m ensurepip
RUN python3 -m pip install --upgrade pip setuptools

WORKDIR /psw_api

COPY . /psw_api/

RUN pip --no-cache-dir install -r requirements.txt

CMD ["python3", "main.py"]