from sqlalchemy import Column, String, Integer, ForeignKey, Date, Numeric
from src.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Customer(Base):
    __tablename__ = "customer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    currency_code = Column(String(3), nullable=False)

