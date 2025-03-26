FROM python:3.192

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir requerimientos.txt

COPY main.py ./

CMD ["python", "main.py"]
