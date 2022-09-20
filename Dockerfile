FROM python:3.7

ARG VERSION

LABEL org.label-schema.version=$VERSION

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY app/* /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

