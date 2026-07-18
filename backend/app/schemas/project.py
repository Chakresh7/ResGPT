import uuid
from datetime import datetime

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    description: str | None = None


class ProjectOut(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    description: str | None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
