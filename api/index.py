from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from db import test_connection
import os

app = FastAPI(docs_url=None, redoc_url=None)

# Get the api/ directory path
api_dir = os.path.dirname(os.path.abspath(__file__))

# Mount the api/ directory itself for static files (served at /api/static)
app.mount("/api/static", StaticFiles(directory=api_dir), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = os.path.join(api_dir, "index.html")
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