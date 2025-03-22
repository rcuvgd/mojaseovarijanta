from fastapi import APIRouter, HTTPException
from app.schemas.client_schema import ClientCreate, ClientResponse
from app.services.client_service import create_client

router = APIRouter()

@router.post("/", response_model=ClientResponse)
def add_client(client_data: ClientCreate):
    try:
        return create_client(client_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
