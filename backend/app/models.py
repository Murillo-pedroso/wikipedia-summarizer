from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True, nullable=False)
    summary = Column(Text, nullable=False)
