import uuid
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.db.base_model import Base
from app.models.draft_model import Draft
from app.schemas.draft_schema import DraftCreate, DraftResponse
from typing import List

def get_client_db_path(client_id: str) -> str:
    return os.path.join("clients", client_id, "data.db")

def create_draft(client_id: str, site_id: str, draft_data: DraftCreate) -> DraftResponse:
    db_path = get_client_db_path(client_id)
    db_url = f"sqlite:///{db_path}"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)

    db = Session(bind=engine)

    draft_id = str(uuid.uuid4())
    new_draft = Draft(
        draft_id=draft_id,
        site_id=site_id,
        title=draft_data.title,
        slug=draft_data.slug,
        content=draft_data.content,
        meta_description=draft_data.meta_description,
        featured_image=draft_data.featured_image,
        status=draft_data.status,
        scheduled_for=draft_data.scheduled_for
    )

    db.add(new_draft)
    db.commit()
    db.refresh(new_draft)
    db.close()

    return DraftResponse(
        draft_id=draft_id,
        title=new_draft.title,
        slug=new_draft.slug,
        status=new_draft.status,
        scheduled_for=new_draft.scheduled_for
    )

def get_drafts(client_id: str, site_id: str) -> List[DraftResponse]:
    db_path = get_client_db_path(client_id)
    db_url = f"sqlite:///{db_path}"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)

    db = Session(bind=engine)
    drafts = db.query(Draft).filter(Draft.site_id == site_id).all()
    db.close()

    return [
        DraftResponse(
            draft_id=d.draft_id,
            title=d.title,
            slug=d.slug,
            status=d.status,
            scheduled_for=d.scheduled_for
        )
        for d in drafts
    ]
