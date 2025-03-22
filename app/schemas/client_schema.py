from pydantic import BaseModel, EmailStr

class ClientCreate(BaseModel):
    name: str
    domain: str
    contact_email: EmailStr

class ClientResponse(BaseModel):
    client_id: str
    message: str
