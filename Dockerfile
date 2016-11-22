#FROM resin/rpi-raspbian:jessie-20160831  
FROM python:2.7.12
RUN apt-get update
RUN apt-get -qy install curl ca-certificates python sysstat
ADD ./get-pip.py .
ADD ./logstash_test.py .
RUN python get-pip.py 

RUN pip install python-logstash
RUN pip install psutil

CMD ["python", "logstash_test.py"] 
