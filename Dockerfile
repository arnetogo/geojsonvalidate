FROM ubuntu
RUN apt-get update
RUN apt-get install -y software-properties-common python-pip nodejs npm
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN npm install geojson-validation -g
COPY app.py ./
CMD [ "python", "-u", "./app.py" ]
