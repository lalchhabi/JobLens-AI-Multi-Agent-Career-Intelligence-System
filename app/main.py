# Import libraries
from fastapi import FastAPI

# Import project files
from api.routes import router

app = FastAPI(
    title='JobLens AI',
    description="AI career Intelligence System",
    version="1.0.0"

)

app.include_router(router)