# Flask on Docker


This is a simple Hello World application written in Python using the popluar Flask microframework and Docker. In this description we will go through the entire process of building a simple webservice that will run on docker. This is a guide on how to re-create the Hello World application from scratch. Along the way I will provide comments to explain various topics in depth. The main purpose of this project is strictly educational - and primarily for my own experience - but is also intended to help others getting started with flask and docker applications. 


## Who is the target audience?

* Students
* Programmers
* Software developers
* Entrepreneurs
* Anyone with an interest in Python and programming in general
* Python, FLask and Docker beginners


## Prerequisites

* A Mac, Windows or Linux machine
* Some coding experince
* Little knowledge of python, Flask, Docker and Git
* Basic understanding with the command line


## Requirements

* Docker installed 
* Python installed
* Git installed
* Git command line installed



## Project file structure

TODO: Show image



## Build and run the project

1. First, make sure Docker is running locally on your computer

2. Clone the github repository to a directory on your computer

3. Change directory to the root of the project `cd path/to/your/project`

4. Build a Docker image `Docker build -t random_image_name .`

   * `-t` lets you specify an image name. It will otherwise default to a random hash value
   
   * `.` This tells Docker to build an image from your current directory
   
5. Run a container from image `Docker run --rm --name random_container_name -p 8000:5000 image_name`

   * `--rm` deletes the container on exit
   
   * `--name` lets you specify a container name
   
   * `-p` lets you port forward from the containers exposed port(s) to your machine. host_port:container:port
   
   * `image_name` lastly you enter a random image name created from the Docker build command
   
6. Open your browser and go to http://localhost:8000. It should diplay Hello World



## Stopping the project - removing old images and containers

Everytime you build a new image or create a new container from an image, those images or containers are srored on your computer and it is up to you to delete those files once in a while. Otherwise it will take up memory.

When you have a container running all you have to do to quit is type `ctrl C`.

But stopping the container will not remove it. I have managed to find a hacky solution to remove images and containers. But i really don't think it's the optimal way. So hopefully i will come back and update this section once i find a better solution. Untill then this will have to do

   
   * Deleting Docker images

      * `docker images` prints out all images on your computer. This list can either be empty or contain many images. To force       remove all images use the following command
      
      * `docker rmi -f $(docker images -qf dangling=true)` deletes all unused docker images

      * `docker rmi -f image_id`. Deletes a single image by it's id
   
   
   * Deleting Docker containers

      * `docker ps` lists all running containers and their id's. To stop a container simply type

      * `docker stop conatiner_id`


## Inspecting the Dockerfile

TODO:

```python
# 1. Use an official Python runtime as a parent image
FROM python:3-slim


# 2. Create a working directory
WORKDIR app/
RUN mkdir app


# 3. Copy /app % requirements.txt into th containers working directory
COPY ./app app/
COPY requirements.txt .


# 4. install dependencies from requirements.txt
RUN pip install -r requirements.txt


# 5. specify the port number the container should expose
EXPOSE 5000


# 6. Run app.py when the container launches
CMD python app/app.py
```

I have labeled every step with a number and will try to explain what goes on for every line. 
OBS: This is not a 'how to make a Dockerfile'. This Dockerfile is a barebone example on a Dockerfile that will work for this particularly  project.

1. The `FROM` instruction sets the base image for the subsequent instructions. A valid Dockerfile must start with a FROM instruction. Images can be foud at DockerHub.

2. First line creates a working directory calles /app. Next line makes a new directory called app which we will use next.

3. First line copies everything from the /app directory of our application to the newly created app/ directory. Then we copy the requirements.txt to the current directory.

4. Runs a command to install dependecies specified in requirements.txt

5. Specify the port on which the image should be exposed to. By default Flask applications always run on port 5000. It is worth noting that this line doesn't actually do anything. It is only there to help the developer see what ports are exposed. It is up to the developer to actually expose the port when using the `docker run` command.

6. The last `CMD` instuction rund the main file which will start the server.


## Using venv

TODO: What is venv? Why use venv? How to use venv?


## Exclude any unnecessary files (.gitignore)

TODO: 
