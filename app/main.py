# What just happened when you run the app:
# models is imported
# Task is registered with Base
# create_all() walks the registry
# SQLite file tasks.db is created
# Table tasks is created (if not already present)
# This runs once.
# Future runs see the table and do nothing.


from fastapi import FastAPI
from app.database import engine
from app import models
from .routes import router

app = FastAPI()

# Create tables at startup
models.Base.metadata.create_all(bind=engine)

@app.get("/ping")
def ping():
    return {"status": "ok"}

app.include_router(router)
