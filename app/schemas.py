from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: Optional[datetime] = None
    status: Optional[str] = "Pending"


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None  
    due_date: Optional[datetime] = None  # Changed from str to datetime


class TaskResponse(TaskCreate):
    id: str
    created_at: datetime
    class Config:
        from_attributes = True  # Changed from orm_mode to from_attributes
