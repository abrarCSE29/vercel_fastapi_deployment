from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from db import test_connection
import os

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r") as f:
        return HTMLResponse(content=f.read())


@app.get("/api")
def api_root():
    return {"message": "Hello from FastAPI on Vercel!"}


@app.get("/api/health")
def health_check():
    db_status = test_connection()
    return {
        "status": "healthy",
        "database": db_status,
    }