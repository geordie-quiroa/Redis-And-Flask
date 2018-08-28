FROM python:3.6-alpine
#FROM python:3.6-ubuntu:latest
#RUN apt-get update \
#  && apt-get install -y python3-pip python3-dev \
#  && cd /usr/local/bin \
#  && ln -s /usr/bin/python3 python \
#  && pip3 install --upgrade pip \
ENTRYPOINT ["python3"]
ENV APP_HOME=/app
LABEL MAINTAINER="Geordie Quiroa" EMAIL="gqmail@protonmail.com"
WORKDIR ${APP_HOME}
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
# COPY src dest
COPY . ${APP_HOME}/
CMD ["./__init__.py"]
EXPOSE 555
