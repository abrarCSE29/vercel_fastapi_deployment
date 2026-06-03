from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from db import test_connection
import os

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

# Serve static files from the public/ directory
public_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")
if os.path.isdir(public_path):
    app.mount("/public", StaticFiles(directory=public_path), name="public")


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = os.path.join(public_path, "index.html")
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