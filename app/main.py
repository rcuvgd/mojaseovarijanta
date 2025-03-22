from fastapi import FastAPI
from app.routers import clients

app = FastAPI(title="SEO Tracker")

app.include_router(clients.router, prefix="/clients", tags=["Clients"])
