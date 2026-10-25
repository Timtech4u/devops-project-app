# Counter App

This is a simple counter application with a Python/Flask backend and an HTML/CSS/JavaScript frontend.

## Project Structure

- `backend/`: Contains the Flask backend application.
- `frontend/`: Contains the HTML/CSS/JavaScript frontend application.
- `Jenkinsfile`: Jenkins pipeline configuration.

## Running the Application

### Using Docker

1. Build and run the backend:
    ```sh
    cd backend
    docker build -t counter-backend .
    docker run -d -p 5555:5555 counter-backend
    ```

2. Build and run the frontend:
    ```sh
    cd frontend
    docker build -t counter-frontend .
    docker run -d -p 80:80 counter-frontend
    ```

3. Open your browser and go to `http://localhost`.

### Using Jenkins

1. Create a new Jenkins pipeline job.
2. Configure the pipeline to use the `Jenkinsfile` from this repository.
3. Run the pipeline to build both backend and frontend Docker images.

## Backend dependency verification

The backend uses Python 3.11 and a fully pinned dependency file generated from
`backend/requirements.in`. Flask, Werkzeug and Flask-CORS are upgraded together.

```sh
python3.11 -m venv .venv
. .venv/bin/activate
pip install -r backend/requirements.txt
PYTHONPATH=backend python -m unittest discover -s backend/tests -v
pip check
```

Tests cover counter updates, the frontend CORS preflight and rejection of implicit
private-network access. Refresh dependencies with
`uv pip compile --upgrade --python 3.11 backend/requirements.in -o backend/requirements.txt`.
