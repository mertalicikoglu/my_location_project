# Location Data API with FastAPI and PostgreSQL

## Overview
This project is a RESTful API developed using FastAPI and PostgreSQL to store and retrieve location data. The API provides endpoints for adding new location data and retrieving existing location records. The main focus is on providing a reliable and scalable solution for location-based data services. The application is designed with containerization in mind using Docker.

## Features
- CRUD operations for location data.
- FastAPI as the web framework for high performance.
- PostgreSQL as the database for persistent storage.
- Dockerized application to ensure easy deployment and environment consistency.
- Celery integrated for asynchronous task handling (such as background data processing).

## Technologies Used
- **Python** (FastAPI, SQLAlchemy, Pydantic)
- **PostgreSQL** for database management.
- **Docker** for containerization.
- **Celery** with **RabbitMQ** for asynchronous tasks.
- **pytest** for unit testing.

## Setup Instructions
### Prerequisites
- Docker and Docker Compose
- Git
- Python 3.9+

### Installation Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/mertalicikoglu/my_location_project.git
   cd my_location_project
   ```

2. **Environment Variables**
   Create a `.env` file to store your environment variables:
   ```sh
   POSTGRES_USER=myuser
   POSTGRES_PASSWORD=mypassword
   POSTGRES_DB=location_data
   ```

3. **Build and Start the Docker Containers**
   ```sh
   docker-compose up --build
   ```
   This command will start the PostgreSQL, RabbitMQ, and FastAPI application in containers.

4. **Access the API**
   Once the application is up, you can access it at `http://localhost:8000`.

### Running Tests
- Ensure your Docker containers are running.
- Use pytest to run unit tests:
  ```sh
  pytest tests/
  ```

## API Endpoints
### 1. Add New Location (Async)
- **URL**: `/locations/async/`
- **Method**: `POST`
- **Description**: Add a new location record to be processed asynchronously.

### 2. Get All Locations
- **URL**: `/locations/`
- **Method**: `GET`
- **Description**: Retrieve all stored location records.

## Directory Structure
```
.
├── app
│   ├── main.py          # FastAPI application entry point.
│   ├── models.py        # Database models using SQLAlchemy.
│   ├── schemas.py       # Pydantic schemas for data validation.
│   ├── database.py      # Database configuration.
│   └── tasks.py         # Celery tasks for asynchronous operations.
├── tests
│   └── test_locations.py # Unit tests for location-related API endpoints.
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Development
To start the development server, use the following command:
```sh
uvicorn app.main:app --reload
```
This will start the server at `http://127.0.0.1:8000` and automatically reload for any code changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions
Contributions are welcome! Please open a pull request or an issue if you have suggestions or encounter any problems.

## Contact
For any inquiries or questions, please reach out to [alicikoglumert@gmail.com].

