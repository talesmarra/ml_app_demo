FROM python:3.7

COPY requirements.txt ./app/requirements.txt

EXPOSE 8501

COPY app/app.py /app/app.py

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "streamlit", "run" ]

CMD ["app.py"]