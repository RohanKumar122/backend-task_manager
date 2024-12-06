from fastapi import APIRouter, HTTPException, Depends
from app.database import db,tasks_collection
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from bson import ObjectId
from datetime import datetime
from typing import Optional
from app.auth import get_current_user


router = APIRouter(prefix="/tasks", tags=["Tasks"])

def validate_object_id(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid task ID")
    return ObjectId(id)

@router.get("/tasks")
async def get_tasks(current_user: str = Depends(get_current_user)):
    try:
        tasks = list(tasks_collection.find({"user": current_user})) 
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching tasks")


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, token: str = Depends(get_current_user)):
    task_dict = task.dict()
    task_dict["created_at"] = datetime.utcnow()
    result = db.tasks.insert_one(task_dict)
    task_dict["_id"] = str(result.inserted_id)
    return TaskResponse(id=str(result.inserted_id), **task_dict)

@router.get("/", response_model=list[TaskResponse])
def get_tasks(status: Optional[str] = None, token: str = Depends(get_current_user)):
    query = {"status": status} if status else {}
    tasks = list(db.tasks.find(query))
    for task in tasks:
        task["id"] = str(task.pop("_id"))
    return tasks

@router.get("/order-by-due-date", response_model=list[TaskResponse])
def get_tasks_ordered_by_due_date(token: str = Depends(get_current_user)):
    tasks = list(db.tasks.find().sort("due_date", 1))
    for task in tasks:
        task["id"] = str(task.pop("_id"))
    return tasks

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, task: TaskUpdate, token: str = Depends(get_current_user)):
    task_id = validate_object_id(task_id)
    
    update_data = {k: v for k, v in task.dict(exclude_unset=True).items()}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No data to update")

    result = db.tasks.find_one_and_update(
        {"_id": task_id},  
        {"$set": update_data}, 
        return_document=True, 
    )

    if not result:
        raise HTTPException(status_code=404, detail="Task not found")

    result["id"] = str(result.pop("_id"))
    
    return TaskResponse(**result)  


@router.delete("/{task_id}")
def delete_task(task_id: str, token: str = Depends(get_current_user)):
    task_id = validate_object_id(task_id)
    result = db.tasks.delete_one({"_id": task_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
