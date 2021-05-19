# This image was created to listen for those UDP packets and store the information in a log file.

FROM python:3.7-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./udplistener.py .
CMD ["udplistener.py"]
ENTRYPOINT ["python"]