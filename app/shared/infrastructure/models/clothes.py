from sqlalchemy import Column, String, UUID

from database.tools.sqlalchemy.orm import Base
from shared.infrastructure.models.audit_fields import AuditFields


class Clothes(Base, AuditFields):
    __tablename__ = "clothes"

    id = Column(UUID(as_uuid=True), primary_key=True)
    file_path = Column(String, nullable=False)
