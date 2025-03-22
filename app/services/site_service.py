import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.models.site_model import Site
from app.schemas.site_schema import SiteCreate, SiteResponse
from app.db.base_model import Base
import os

def get_client_db_path(client_id: str) -> str:
    return os.path.join("clients", client_id, "data.db")

def create_site_for_client(client_id: str, site_data: SiteCreate) -> SiteResponse:
    db_path = get_client_db_path(client_id)
    db_url = f"sqlite:///{db_path}"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)  # osiguraj da tabela postoji

    db = Session(bind=engine)

    site_id = str(uuid.uuid4())
    new_site = Site(
        site_id=site_id,
        client_id=client_id,
        name=site_data.name,
        domain=site_data.domain,
        system_type=site_data.system_type,
        api_url=site_data.api_url,
        api_key=site_data.api_key,
        status="active"
    )

    db.add(new_site)
    db.commit()
    db.refresh(new_site)
    db.close()

    return SiteResponse(
        site_id=site_id,
        name=new_site.name,
        domain=new_site.domain,
        system_type=new_site.system_type,
        status=new_site.status
    )

def get_sites_for_client(client_id: str) -> List[SiteResponse]:
    db_path = get_client_db_path(client_id)
    db_url = f"sqlite:///{db_path}"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)

    db = Session(bind=engine)
    sites = db.query(Site).filter(Site.client_id == client_id).all()
    db.close()

    return [
        SiteResponse(
            site_id=s.site_id,
            name=s.name,
            domain=s.domain,
            system_type=s.system_type,
            status=s.status
        )
        for s in sites
    ]

