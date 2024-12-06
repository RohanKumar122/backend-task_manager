from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt 
# from jwt.exceptions import ExpiredSignatureError, InvalidTokenError  
from datetime import datetime, timedelta
import os
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_secret_key") 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str

class UserInDB(User):
    password: str

fake_users_db = {
    "testuser": {
        "username": "test",
        "password": "password"  
    }
}

def verify_password(plain_password: str, password: str) -> bool:
    
    return plain_password == password

def get_user(db: dict, username: str) -> UserInDB | None:
    user_dict = db.get(username)
    if user_dict:
        return UserInDB(**user_dict)
    return None

def authenticate_user(username: str, password: str) -> UserInDB | None:
    user = get_user(fake_users_db, username)
    if user and verify_password(password, user.password):
        return user
    return None

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
        return User(username=username)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

@app.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user.username}!"}
