# Task Management API  

This is a backend application for managing tasks using **FastAPI** and **MongoDB**.

## Features  
- User Signup and Signin with JWT-based authentication.  
- Create, update, retrieve, and delete tasks.  
- Filter tasks by status and sort them by due date or creation time.  
- MongoDB database integration with proper indexing for efficient queries.  
- API documentation using Swagger.  
- Error handling with meaningful messages.  

---

## Prerequisites  
- Python 3.10 or above  
- MongoDB (Atlas or Local)  

---

## Tech Stack  
- **Backend Framework**: FastAPI  
- **Database**: MongoDB (using pymongo)  
- **Authentication**: JWT-based token system  

---

## Installation  

### Clone the Repository  
```bash  
git clone https://github.com/yourusername/task-management-api.git  
cd task-management-api

```

### setup Virtual Environment
```bash
python -m venv venv  
venv/Scripts/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt  
```

### Create .env file
- Add MONGO_URI = mongodb://localhost:27017/

### RUN the application
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload  
```



