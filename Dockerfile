FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask

COPY script.py .

CMD ["python3","script.py"]