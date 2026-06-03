from fastapi import FastAPI
from db import test_connection

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

@app.get("/api")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/health")
def health_check():
    db_status = test_connection()
    return {
        "status": "healthy",
        "database": db_status
    }
