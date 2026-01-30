"""
Customer model
"""

from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class Customer(Base):
    """Customer database model"""

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    country = Column(String, index=True)
    city = Column(String)
    signup_date = Column(Date, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
