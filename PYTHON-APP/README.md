# PYTHON.MD CONFIG
#### Use the official Python image as a base image
FROM python:3.9-slim

### Set the working directory inside the container
WORKDIR /app

### Copy the current directory contents into the container at /app
COPY . /app


### Make port 5000 available to the world outside this container
EXPOSE 5000

### Define environment variable
ENV NAME World

### Run app.py when the container launches
CMD ["python", "app.py"]

# PYTHOM CODE

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():

    return 'THANKS YOU 3MTT THANK YOU UTIVA THANK YOU MR LATEEF'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)