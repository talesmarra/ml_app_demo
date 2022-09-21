FROM python:3.7

ARG VERSION

LABEL org.label-schema.version=$VERSION

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY app/main.py /app/main.py

COPY app/model/ /app/model/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

