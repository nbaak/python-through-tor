FROM python:3.10.2

RUN python -m pip install requests requests[socks]
RUN mkdir /application

COPY ./src /application

WORKDIR /application
ENTRYPOINT ["/application/App.py"]