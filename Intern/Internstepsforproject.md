# Steps taken in doing assignment

## 1. Setting up your local repository 

Clone the github repository with the project by running the command 
```
git clone https://github.com/Timtech4u/devops-project-app.git 
``` 

Once the repository is cloned, ensure it appears in your local repository and is saved in and ensure you are working with the same directory . You can run the commands to do the following: 
Print current work directory: Check what work environment youre in.
```
pwd
```
Change current work directory: To work within the local repository of the project. by running cd path/to/your/repository where the devops-project-app is the repo. 

```
cd devops-project-app 
```
Ensure the dirctory appears in your visual code window
```
code .
#or
code path/to/your/repository
```
Once you are within the right work environment you can start the following

## 2. Running the APP

### Running the front end
To run the app, you can download a live server to view the user interface ie your index.html file 

### Running the backend with docker. I.e Creating an image.

Ensure to run the Dockerfile ```(Docker should be installed on your system)```, which contains a set of instructions (requirements.txt) used by Docker to build an image and run a container. 

### Build the docker image
 ```
 docker build -t app .
 ```
### Run the Docker container ("app" in code block, refers to the name of my backend app file without its extension)
```
docker run -p 5555:5555 app

 ```
 making sure the port mapping is the same as that in your app file.
 
You can check docker status, container_id and stop the container after by using the commands
```
docker --version
docker --ps
docker stop container_id
```
Your container_id is the one you can get from running the second code



#### Dockerfile Instructions used when running the above
Each code representation that is being run when you do a docker build is explained below. Our goal is to build the flask app using a docker image 

##### The Flask app (Backend app)
[Flask app image](Intern\flaskappimage.png)

##### The docker image requirements
[Image of requirements](Intern\Image_of_requirements.png)

##### Docker build instructions, using the flask app, requirements, app run command. 

```
FROM python:3.8-slim
```
This line specifies the base image to use for the Docker image. python:3.8-slim is a lightweight version of Python 3.8.

```
WORKDIR /app
```
This sets the working directory inside the Docker container to /app. All subsequent instructions will be run from this directory.
```
COPY requirements.txt requirements.txt
```

This copies the requirements.txt file from your local machine to the /app directory in the Docker image.
```
RUN pip install -r requirements.txt
```
This installs the Python dependencies listed in requirements.txt into the Docker image.

```
COPY . .
```
This copies all the files from your local directory to the /app directory in the Docker image

```
CMD ["python", "app.py"]
```
This sets the default command to run when the container starts. In this case, it will run python app.py.


## 3. Testing the app

Once the front end and back end local hosts are opened in your browser, using the app should get the correct responses on the front end and back end 
[Output of web app](Intern\display_of_running_app.png)
