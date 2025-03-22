from sqlalchemy import Column, String
from app.db.base_model import Base

class Client(Base):
    __tablename__ = "clients"

    client_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    domain = Column(String)
    contact_email = Column(String)
