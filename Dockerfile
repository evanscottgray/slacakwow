# SlackWow
#
# VERSION               0.0.1

FROM ubuntu
MAINTAINER Evan Gray <hello@evanscottgray.com>

RUN apt-get update && apt-get install -y python curl git && curl https://bootstrap.pypa.io/get-pip.py | python -

ENTRYPOINT git clone https://github.com/evanscottgray/slackwow.git && \
               cd slackwow && \
               pip install -r requirements.txt && \
               python app.py

EXPOSE 5000
