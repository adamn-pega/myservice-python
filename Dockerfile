FROM ubuntu:latest

COPY . .
RUN apt-get update && apt-get install -y python3.10 python3.10-dev python3-pip
RUN pip3 install -r requirements.txt

CMD ["python3", "server.py"]