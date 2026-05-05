from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.endpoints import router as audit_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audit_router, prefix="/api", tags=["Audit"])

@app.get("/")
async def root():
    return {"message": "Network Scanner API is Active"}