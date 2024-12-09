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

---

### Testing API Endpoints with POSTMAN ( make sure you have RUN the backend code on PORT 8000)

#### 1. **Get Token**

   To get the token, follow these steps:

   1. **Create a New Collection in POSTMAN**  
      Open POSTMAN and create a new collection named **Task Manager**.

   2. **Add a Request to Get the Token**  
      - **Method**: `POST`  
      - **API Endpoint**: `http://localhost:8000/token`  
      - **Credentials**:  
        - **Username**: `testuser`  
        - **Password**: `password`

   3. **Response**  
      On sending the request, you will receive a response with the following details:
      ```json
      {
        "access_token": "<YOUR TOKEN>",
        "token_type": "bearer"
      }
      ```

   4. **Copy the Token**  
      Copy `<YOUR TOKEN>`, then go to the **Authorization** section in POSTMAN and add it as a **Bearer Token**.

   5. **Token Expiry**  
      The token will be valid for the next 30 minutes.

---

#### 2. **Get All Tasks**

   - **Method**: `GET`  
   - **API Endpoint**: `http://localhost:8000/tasks`

---

#### 3. **Create Task**

   - **Method**: `POST`  
   - **API Endpoint**: `http://localhost:8000/tasks`  
   - **Request Body**:  
     ```json
     {
       "title": "string",
       "description": "string",
       "due_date": "2024-12-10T12:00:00",
       "status": "Done",
       "created_at": "2024-12-07T14:53:00.215000"
     }
     ```

---

#### 4. **Update Task**

   - **Method**: `PUT`  
   - **API Endpoint**: `http://localhost:8000/tasks/<id>`  
   - **Request Body**:  
     ```json
     {
       "title": "<updated string>",
       "description": "string",
       "due_date": "2024-12-10T12:00:00",
       "status": "Done",
       "created_at": "2024-12-07T14:53:00.215000"
     }
     ```

---

#### 5. **Delete Task**

   - **Method**: `DELETE`  
   - **API Endpoint**: `http://localhost:8000/tasks/<id>`  
   - **Response**:  
     ```json
     {
       "message": "Task deleted"
     }
     ```










