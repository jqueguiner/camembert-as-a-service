FROM guignol95/ai_apis

RUN apt-get update && apt-get install -y --no-install-recommends \
  python-opencv \
  python-matplotlib \
  python-pillow 


ADD src /src

WORKDIR /src

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]

