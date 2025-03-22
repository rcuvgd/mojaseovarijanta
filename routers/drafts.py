from fastapi import APIRouter, HTTPException
from app.schemas.draft_schema import DraftCreate, DraftResponse
from app.services.draft_service import create_draft, get_drafts
from typing import List

router = APIRouter()

@router.post("/{client_id}/sites/{site_id}/drafts", response_model=DraftResponse)
def add_draft(client_id: str, site_id: str, draft_data: DraftCreate):
    try:
        return create_draft(client_id, site_id, draft_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{client_id}/sites/{site_id}/drafts", response_model=List[DraftResponse])
def list_drafts(client_id: str, site_id: str):
    try:
        return get_drafts(client_id, site_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

