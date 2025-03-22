import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.schemas.client_schema import ClientCreate, ClientResponse
from app.models.client_model import Client
from app.db.base_model import Base
from app.utils.file_utils import create_client_folder

def create_client(client_data: ClientCreate) -> ClientResponse:
    client_id = str(uuid.uuid4())
    path = create_client_folder(client_id)

    db_url = f"sqlite:///{path}/data.db"
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)

    db = Session(bind=engine)
    db_client = Client(
        client_id=client_id,
        name=client_data.name,
        domain=client_data.domain,
        contact_email=client_data.contact_email
    )
    db.add(db_client)
    db.commit()
    db.close()

    return ClientResponse(client_id=client_id, message="Klijent kreiran i spreman za rad.")
