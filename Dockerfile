# This image contains a baseline model for eye fundus disease detection prediction and detection on color fundus eye images
# Author: Arkangel AI
# Developer: Daniel Lopez

# set base image (host OS)
FROM python:3.8

RUN apt-get update && apt-get install -y git python3-dev gcc libgl1-mesa-glx\
    && rm -rf /var/lib/apt/lists/* 

# set the working directory in the container
RUN mkdir /app
WORKDIR /app

# copy the dependencies file to the working directory
ADD requirements.txt /app
# ADD .env /app
RUN ls -a /app/
# install dependencies
RUN pip3 install -r requirements.txt

#set diabetic retinopathy API environment variable
ENV URL_RETINOPATIAS https://api-diabetes-ojo-x6tz36c4ga-uc.a.run.app/prediction

# copy the content of the local src directory to the working directory
ADD . /app
RUN ls ./app
EXPOSE 8080
RUN chmod +x ./entrypoint.sh
# command to run on container start
ENTRYPOINT [ "sh", "entrypoint.sh" ]