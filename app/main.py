# Import libraries
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Import project files
from api.routes import router

app = FastAPI(
    title='JobLens AI',
    description="AI career Intelligence System",
    version="1.0.0"
)

# Serve static files
app.mount("/static", StaticFiles(directory="ui/static"), name =
              "static")

app.include_router(router)
