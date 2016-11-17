FROM resin/rpi-raspbian:jessie-20160831  
RUN apt-get update && \  
    apt-get -qy install curl ca-certificates python
ADD . .
RUN python get-pip.py 
RUN pip install python-logstash
CMD ["python", "logstash.py"] 
