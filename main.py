from fastapi import FastAPI
from routes import router

# create the fastAPI class instance
app = FastAPI()
app.include_router(router)
