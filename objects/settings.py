from pydantic import BaseModel, Field

from typing import Optional


class Settings(BaseModel):
    serviceName: str
    versionName: str
    adsByGoogleId: Optional[str] = Field(None)
    contactEmail: str
