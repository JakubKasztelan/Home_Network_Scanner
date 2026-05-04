from fastapi import FastAPI
from api.endpoints import router as audit_router

app = FastAPI()

app.include_router(audit_router, prefix="/api", tags=["Audit"])

@app.get("/")
async def root():
    return {"message": "Network Scanner API is Active"}