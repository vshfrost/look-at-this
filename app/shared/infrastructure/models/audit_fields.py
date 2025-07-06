from datetime import datetime, timezone

from sqlalchemy import Column, DateTime


class AuditFields:
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
