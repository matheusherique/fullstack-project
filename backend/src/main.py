from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.router import router as auth_router
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

tags_metadata = [
    {"name": "Users", "description": "Operations related to user management"}
]

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
