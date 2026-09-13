# Docker Python App 🐳

A simple Python Flask web application containerized with Docker and deployed using a production-ready Gunicorn server.

## 🚀 Project Overview

This project demonstrates the fundamentals of containerizing a Python web application using Docker.

The application runs inside a lightweight Docker container and is exposed on port `5000`.

## 🛠️ Technologies Used

* Python 3.10
* Flask
* Gunicorn
* Docker
* Git & GitHub

## 📁 Project Structure

```text
docker-python-app/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🏗️ Architecture

```text
User
  │
  │ HTTP Request
  ▼
Docker Container
  │
  ├── Gunicorn
  │     │
  │     ▼
  │   Flask App
  │     │
  │     ▼
  │   app.py
  │
  ▼
Port 5000
  │
  ▼
Browser
```

## 🐳 Docker Configuration

The Dockerfile uses `python:3.10-slim` as the base image.

The application dependencies are installed from `requirements.txt`, and Gunicorn is used as the production WSGI server.

## ▶️ Run Locally Without Docker

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## ▶️ Run With Docker

Build the Docker image:

```bash
docker build -t docker-python-app:v2 .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name docker-python-container --restart unless-stopped docker-python-app:v2
```

Check the running container:

```bash
docker ps
```

View application logs:

```bash
docker logs docker-python-container
```

Open the application:

```text
http://localhost:5000
```

## 🔍 Useful Docker Commands

Stop the container:

```bash
docker stop docker-python-container
```

Start the container:

```bash
docker start docker-python-container
```

Remove the container:

```bash
docker rm docker-python-container
```

List Docker images:

```bash
docker images
```

## 🎯 DevOps Skills Demonstrated

This project demonstrates:

* Python application containerization
* Docker image creation
* Docker container management
* Port mapping
* Docker restart policies
* Dependency management
* Production WSGI server with Gunicorn
* Git version control
* GitHub repository management

## 📌 Future Improvements

The project can be extended with:

* Docker Compose
* CI/CD using GitHub Actions
* Jenkins pipeline
* Automated testing
* Docker image publishing
* Cloud deployment

## 👩‍💻 Author

**Maryam Khanum**

DevOps Portfolio Project — Project 1
