FROM python:2.7
WORKDIR /code

RUN pip install influxdb jsonpath_rw statistics psutil pathlib fhirclient numpy monotonic jq
RUN pip install gevent==1.2.2
RUN pip install -e git://github.com/locustio/locust.git@0.12.2#egg=locustio
#RUN pip install locust==0.14.6
RUN apt-get update
RUN apt-get install -y jq
EXPOSE 4080 
COPY performance_testscripts/ ./performance_testscripts/
COPY start_performance_test.sh .
COPY synthea_output_1_00001-00100 .
CMD ["./start_performance_test.sh", "--backend", "mongo", "--host", "http://localhost:4080","--influxdb", "http://grafana:9068"]
