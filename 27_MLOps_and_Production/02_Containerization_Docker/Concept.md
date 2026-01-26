# Docker and Containers

## 1. The Matrix from Hell
*   Dev Environment: Mac with Python 3.10.
*   Prod Environment: Linux Server with Python 3.6.
*   **Result**: "ModuleNotFoundError".

## 2. Container
A standard unit of software. It packages the code + dependencies + OS settings.
*   **Image**: The blueprint (Read-only).
*   **Container**: The running instance (Writable layer on top).

## 3. The Dockerfile
Steps to build the image.
1.  `FROM python:3.9` (Base OS).
2.  `COPY . /app` (Move code inside).
3.  `RUN pip install -r requirements.txt` (Install libs).
4.  `CMD ["python", "app.py"]` (Start).

## 4. Kubernetes (K8s)
Docker manages 1 container. K8s manages 10,000 containers across 100 machines.
*   Self-healing: If a container crashes, K8s restarts it.
*   Scaling: If traffic spikes, K8s adds more copies.
