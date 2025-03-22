from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class DraftCreate(BaseModel):
    title: str
    slug: str
    content: str
    meta_description: Optional[str] = None
    featured_image: Optional[HttpUrl] = None
    status: Optional[str] = "draft"
    scheduled_for: Optional[datetime] = None

class DraftResponse(BaseModel):
    draft_id: str
    title: str
    slug: str
    status: str
    scheduled_for: Optional[datetime]
