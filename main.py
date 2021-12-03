import uvicorn
from fastapi import FastAPI,Path

app = FastAPI()

students = {
    1: {
        "name":"Shital",
        "age" : 25,
        "class" : "BE"
    }
}

@app.get("/")
async def root():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def student(student_id: int = Path(None, description="ID of student you want to view")):
    return students[student_id]




