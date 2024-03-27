# Simple Web App using Docker Compose

## Overview
This project consists of a web application containerized using Docker Compose. It includes three main components:

- 🖥️ **Frontend**: A single-page application to capture user data.
- 🔧 **Backend**: A Flask server that processes data and interacts with the database.
- 💾 **Database**: MongoDB for storing user information.

## Prerequisites
- Docker and Docker Compose
- Any modern web browser

## Running the Application
1. Clone the repository to your local machine.
2. Navigate to the project's root directory.
3. Run the following command to start all services:
   ```
   docker-compose up --build
   ```
4. Open your browser and go to `http://localhost` to view the application.

## Using the Application
1. Enter your name and email address in the provided fields on the webpage.
2. Click the "Submit" button to save the information to the database.
3. Check the logs for a confirmation message indicating successful storage.

## Stopping the Application
- To stop the application and remove all services, run:
  ```
  docker-compose down
  ```

## Components
- **Frontend**: Served using `nginx:alpine` image and accessible on port 80.
- **Backend**: Flask application running on port 5000.
- **MongoDB**: NoSQL database service running on the default port of 27017.

---
👍 Happy Checking!
