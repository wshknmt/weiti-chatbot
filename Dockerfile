FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip python3-venv

RUN python3 -m pip install rasa setuptools wheel spacy

RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:`find / -name 'libcudart.so.11.0'` && \
    . /etc/profile
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
RUN python3 -m spacy download pl_core_news_lg

RUN mkdir app

WORKDIR /app

COPY . .

RUN rasa train
RUN rasa telemetry disable

EXPOSE 8000
EXPOSE 5055

ENTRYPOINT ["bash", "-v", "docker_run_app.sh"]
