from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

@app.get("/api")
def read_root():
    return {"message": "Hello from FastAPI on Vercel!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}