import os

# Define the folder structure
folders = [
    'src/frontend/public',
    'src/frontend/src',
    'src/backend/app',
    'scripts',
    'tests',
    'docs'
]

# Define the files to be created with their content
files = {
    '.gitignore': """# Ignore Python bytecode
__pycache__/
*.pyc

# Ignore Node.js dependencies
node_modules/

# Ignore environment variables
.env
""",
    'docker-compose.yml': """version: '3.8'

services:
  frontend:
    build:
      context: ./src/frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - ./src/frontend:/app
    environment:
      - NODE_ENV=development

  backend:
    build:
      context: ./src/backend
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    volumes:
      - ./src/backend:/app
    environment:
      - FLASK_ENV=development
      - PYTHONUNBUFFERED=1
    depends_on:
      - frontend

volumes:
  db_data:
""",
    '.env': """# Frontend
REACT_APP_API_URL=http://localhost:5000

# Backend
FLASK_ENV=development
SECRET_KEY=your_secret_key
""",
    'README.md': """# Project Name

## Setup

### Prerequisites
- Docker
- Docker Compose

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/niteshldd/ai-content-creator.git
   cd your-repo
Create a .env file in the project root based on the .env.example file.

Build and run the containers:

bash
Copy code
docker-compose up --build
Access the application:

Frontend: http://localhost:3000
Backend: http://localhost:5000
Folder Structure
src/frontend/: Contains the frontend code (React or Vue.js).
src/backend/: Contains the backend code (e.g., Flask, Node.js).
scripts/: Custom scripts for deployment, testing, etc.
tests/: Contains unit, integration, and end-to-end tests.
docs/: Project documentation.
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.
""",
'src/frontend/Dockerfile': """# Use official Node.js image as the base image
FROM node:18-alpine

Set working directory inside the container
WORKDIR /app

Copy package.json and package-lock.json to the working directory
COPY package*.json ./

Install dependencies
RUN npm install

Copy the entire frontend codebase to the working directory
COPY . .

Build the frontend for production
RUN npm run build

Expose the port the app runs on
EXPOSE 3000

Command to run the app
CMD ["npm", "start"]
""",
'src/backend/Dockerfile': """# Use an official Python runtime as a parent image
FROM python:3.10-slim

Set the working directory in the container
WORKDIR /app

Copy the requirements file to the container
COPY requirements.txt .

Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

Copy the entire backend codebase to the working directory
COPY . .

Expose the port that the app will run on
EXPOSE 5000

Command to run the application
CMD ["python", "app/main.py"]
""",
'src/backend/requirements.txt': """# Example Python dependencies
Flask==2.3.2
requests==2.31.0
"""
}


for folder in folders:
  os.makedirs(folder, exist_ok=True)

# Create files with their content
for filepath, content in files.items():
  with open(filepath, 'w') as f:
    f.write(content)

print("Project structure created successfully!")