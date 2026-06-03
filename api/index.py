from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from db import test_connection

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

# Serve static files from public/ directory
app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("public/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/api")
def api_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/health")
def health_check():
    db_status = test_connection()
    return {
        "status": "healthy",
        "database": db_status
    }