# Flask on Docker



This is a simple Hello World application written in Python using the popluar Flask microframework and Docker. In this description we will go through the entire process of building a simple webservice that will run on docker. This is a guide on how to re-create the Hello World application from scratch. Along the way I will provide comments to explain various topics in depth. The main purpose of this project is strictly educational - and primarily for my own experience - but is also intended to help others getting started with flask and docker applications. 

## Who is the target audience?

* Programmers
* Software developers
* Entrepreneurs
* Anyone with an interest in Python and programming in general
* Anyone who wants to learn how to use Flask with Docker

## Prerequisites

* A Mac, Windows or Linux machine
* Some coding experince
* Little knowledge of python, Flask, Docker and Git
* Basic understanding of using the command line

## Requirements

* Docker installed 
* Python installed
* Git installed
* Git command line installed

## Running the project

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

## File structure

TODO: Show image

## Inspecting the Dockerfile

TODO:

## Using venv

TODO: Is it necessary when we use Docker and Why? How to use it for local development?

## Exclude any unnecessary files (.gitignore)

TODO: 
