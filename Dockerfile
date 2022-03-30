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

# opencv 설치를 위해 필요
RUN apt-get install -y libgl1-mesa-glx

RUN apt-get install -y libgtk2.0-dev

#install dependencies
COPY ./src /home/ubuntu
# 배포할 경우 프로젝트 코드를 모두 도커 이미지에 넣는다.
RUN pip install --upgrade pip
RUN pip install --upgrade tensorflow_hub
RUN pip install -r ./requirements.txt