from sqlalchemy import Column, Index, String, Text
from sqlalchemy.dialects.postgresql import UUID

from src.db.base_class import Base


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    country = Column(String(2), nullable=False, unique=False)
    language = Column(String(2), nullable=False, unique=False)   # TODO: Use Enum
    hashed_password = Column(Text, nullable=False, unique=False)


# Define the index on the email field
Index("idx_customers_email", Customer.email)
