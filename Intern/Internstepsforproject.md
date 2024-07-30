# Steps taken in doing assignment

The goal of this project is to automate a docker build of an image by using Jenkins as the automation tool. To automate the building and deployment of the frontend and backend applications, Jenkins automates repetitive tasks, ensuring consistent builds, which enables continuous integration/continuous deployment (CI/CD) practices.


### Step 1: Setting up a virtual machine to install Jenkins on

You can set up Jenkins on your local virtual machine or on a cloud service provider virtual machine. For this task, I used AWS EC2 instance. Then Jenkins can be opened on your web server using the server IP from the virtual machine (VM). Once suggested plugins and admin user is created, you can run your jenkins configuration for the project

After installing the virtual machine run the following commands to install jenkins on the VM


### Step 2: Setting up Jenkins for CI/CD
```
sudo apt update -y #To update the server
sudo apt install openjdk-11-jdk #Jave, a Prequisite for jenkins
```
Next step is to add the repository for Jenkins in our virtual machine by running the commands. These are used to add the Jenkins repository to a Debian-based system's package sources list, allowing you to install Jenkins using the package manager (apt).

```
wget -q -O - https: //pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http: //pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```

Then the next commands are run

```
sudo apt update
sudo apt install jenkins
```

### Start jenkins and check the status

```
sudo systemctl start kenkins
systemctl status jenkins
sudo ufw allow 8080
sudo ufw status
```

## Step 3: Installing docker on the virtual machine 

The virtual machine originally does not have docker on it, but we need it to run in order to build a container in jenkins. Running docker can show if you already have it installed. 

```
docker --version
```
A feedback you may get in jenkins if this isnt done is "Command 'docker' not found, but can be installed with"
```
sudo snap install docker         # version 24.0.5, or
sudo apt  install docker.io      # version 24.0.5-0ubuntu1
sudo apt  install podman-docker  # version 4.7.2+ds1-2build1
```
However a shorter code can be run on linux servers and since we are running an ubuntu machine, we can run this command over manually installing docker. This can be retrived from this repository https: //github.com/docker/docker-install/tree/master
```
curl -fsSL https: //get.docker.com -o get-docker.sh
sh get-docker.sh
``` 

## Step 4: Configure jenkins to use docker
Jenkins upon first configuration may not have the appropriate privileges to access the docker socket to run docker commands. This access allows Jenkins interaction with docker Daemon
```
dockerd-rootless-setuptool.sh install
```

The command is used to set up Docker in rootless mode. Running Docker in rootless mode allows you to run the Docker daemon (dockerd) and containers as a non-root user, enhancing security by reducing the privileges required to run Docker.
Without this configuration, Jenkins may encounter an an error when tryign to run docker commands (See Errors & resolve guide at the bottom of the page)


## Step 5: Updating Javascript backend URL in repository.

By updating the backend URL in the JavaScript, the frontend can correctly communicate with the backend server hosted on a remote IP, ensuring the application works in a production environment. The frontend JavaScript code was initially configured to make API calls to localhost. This works in a local development environment but fails when deployed to a remote server. 

This was run by changing the code 
```
fetch('http:// localhost:5555/counter/increment', { method: 'POST' })
```
to 
```
 fetch('http:// 18.130.110.234:5555/counter/increment', { method: 'POST' })
```


## Step 6 Exposing Ports


## Step 7 Jenkins UI: Building application, checking console output for successful run 

## Step 8: Killing the Virtual machine

##### Insert link toDocumentation for the webapp/image that was automated
