from fastapi import FastAPI
from app.routers import clients, sites, drafts

app = FastAPI(title="SEO Tracker")

app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(sites.router, prefix="/clients", tags=["Sites"])
app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(sites.router, prefix="/clients", tags=["Sites"])
app.include_router(drafts.router, prefix="/clients", tags=["Drafts"])
