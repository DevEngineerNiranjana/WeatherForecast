FROM mongo:latest

# install Python 3.8
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.8
RUN pip3 install pymongo
COPY . /app
WORKDIR /app
RUN python3.8 -m pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3.8"]
CMD ["main.py"]