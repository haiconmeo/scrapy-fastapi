from typing import TYPE_CHECKING
from sqlalchemy import Column,  Integer, String,ForeignKey
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from victim.db.base_class import Base
import datetime
from sqlalchemy.orm import relationship

class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image = Column(String)
    creation_date = Column(DateTime(timezone=True), default=datetime.datetime.now)
    modification_date = Column(DateTime(timezone=True), default=datetime.datetime.now, onupdate=datetime.datetime.now)
    is_active = Column(Boolean, default=True)
    team_id =Column(UUID(as_uuid=True),nullable=True)
    company_id=Column(UUID(as_uuid=True),nullable=True)
    creator_id = Column(Integer, ForeignKey("user.id"))
    creator = relationship("User", back_populates="backgrounds")
