from fastapi import FastAPI

from routers.ClimaRouter import clima_router


from config.database import create_db_and_tables

app = FastAPI()
app.title = "API Clima"
app.version = "1"

@app.on_event("startup")
def on_startup():
    create_db_and_tables()



app.include_router(clima_router)