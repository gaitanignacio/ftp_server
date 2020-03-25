FROM balenalib/jetson-nano-ubuntu-python

WORKDIR /usr/local/src

COPY . .

RUN pip install -r requirements.txt
RUN mkdir /ftp_server
RUN mkdir /ftp_server/jetson

EXPOSE 21

CMD ["python","./server.py"]