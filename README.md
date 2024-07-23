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
