FROM pytorch/pytorch:latest

RUN apt-get update && apt-get install -y --no-install-recommends

ADD src /src

WORKDIR /src

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]

