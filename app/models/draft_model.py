from sqlalchemy import Column, String, Text, ForeignKey, DateTime
from app.db.base_model import Base

class Draft(Base):
    __tablename__ = "drafts"

    draft_id = Column(String, primary_key=True, index=True)
    site_id = Column(String, ForeignKey("sites.site_id"))
    title = Column(String)
    slug = Column(String)
    content = Column(Text)
    meta_description = Column(String)
    featured_image = Column(String)
    status = Column(String, default="draft")  # draft, ready, scheduled, published
    scheduled_for = Column(DateTime, nullable=True)
