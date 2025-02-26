# MediSyncBackend 
This is the backend part of the project, built with Flask, MongoDB, and integrated with a Gen-AI API. It provides a robust and scalable backend to support the frontend application, handle data storage, and leverage AI capabilities.
## Table of Contents
Getting Started

Prerequisites

Installation

Running the Backend

Project Structure

API Endpoints

Database Configuration

Gen-AI API Integration

Contributing

# Getting Started
Before running the backend, ensure you have the following installed:

Python (v3.8 or higher recommended)

MongoDB (local or cloud instance)

pip (Python package manager)

## Installation
Clone the Repository

```bash
  git clone https://github.com/Sami70458/MediSyncBackend.git

```
Navigate to the Project Directory
```bash
  cd mediSyncBackend

```
Create Virtual Environment
```bash
  python -m venv venv

```
Install Dependencies
```bash
  pip install -r requirements.txt

```
Set-Up .env Values
```bash
MONGO_URI=mongodb://localhost:27017/your-database-name
GEN_AI_API_KEY=your-gen-ai-api-key
FLASK_ENV=development
```
Development Server
```bash
python app.py
```
```bash
your-repo-name/backend/
├── app/                 # Main application code
│   ├── __init__.py      # Flask app initialization
│   ├── routes/          # API routes
│   ├── models/          # MongoDB models
│   ├── utils/           # Utility functions (e.g., Gen-AI API integration)
├── tests/               # Unit and integration tests
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── .gitignore           # Files and directories to ignore in Git
└── README.md            # Project documentation
```
# API Generation
Here are the main API endpoints:

Authentication
POST /api/auth/register: Register a new user.

POST /api/auth/login: Log in an existing user.

Data Management
GET /api/data: Fetch all data.

POST /api/data: Add new data.

PUT /api/data/<id>: Update existing data.

DELETE /api/data/<id>: Delete data.

Gen-AI Integration
POST /api/gen-ai/generate: Generate content using the Gen-AI API.
# Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/your-feature-name).

Open a pull request.

