from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import (routers,usersAPI)

app = FastAPI()

# ================= Cross-Origin Resource Sharing (CORS) setting ===============
origins = ["http://localhost:3000","http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ================= Routers inclusion from src directory ===============
app.include_router(routers.router)
app.include_router(usersAPI.router)