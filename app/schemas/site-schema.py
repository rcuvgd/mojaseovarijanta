from pydantic import BaseModel, HttpUrl
from typing import Optional

class SiteCreate(BaseModel):
    name: str
    domain: HttpUrl
    system_type: Optional[str] = "wordpress"  # wordpress, ghost, custom...
    api_url: Optional[HttpUrl] = None
    api_key: Optional[str] = None

class SiteResponse(BaseModel):
    site_id: str
    name: str
    domain: HttpUrl
    system_type: Optional[str]
    status: str = "active"
