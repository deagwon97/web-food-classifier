#set environment variables
FROM tensorflow/tensorflow
 
ENV PYTHONDONTWRITEBYTECODE 1
# ignore buffering
ENV PYTHONUNBUFFERED 1
# set encoding
ENV PPYTHONENCODING utf-8

#set work directory
WORKDIR /home/ubuntu

RUN apt-get update

# for opencv
RUN apt-get install -y libgl1-mesa-glx

RUN apt-get install -y libgtk2.0-dev

#install dependencies
COPY ./src /home/ubuntu

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt