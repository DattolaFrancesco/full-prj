from uuid import uuid4, UUID
from sqlalchemy import Uuid
from sqlalchemy.orm import Mapped,  mapped_column

from app.database import Base

class Counter(Base):
    __tablename__ = "counter"
    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    value: Mapped[int] = mapped_column(default=0)