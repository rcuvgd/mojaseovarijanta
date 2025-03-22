from fastapi import APIRouter, HTTPException, Depends
from app.schemas.site_schema import SiteCreate, SiteResponse
from app.services.site_service import create_site_for_client
from typing import List

router = APIRouter()

@router.post("/{client_id}/sites", response_model=SiteResponse)
def add_site(client_id: str, site_data: SiteCreate):
    try:
        return create_site_for_client(client_id, site_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#from fastapi import 
#from app.services.site_service import get_sites_for_client

@router.get("/{client_id}/sites", response_model=List[SiteResponse])
def list_sites(client_id: str):
    try:
        return get_sites_for_client(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

