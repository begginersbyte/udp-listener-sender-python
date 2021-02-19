FROM alpine:3.7

RUN apk add --update python python-dev py-pip build-base && pip install virtualenv && rm -rf /var/cache/apk/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
CMD ["udplistener.py"]
ENTRYPOINT ["python"]

