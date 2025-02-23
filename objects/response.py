from datetime import datetime

from pydantic import BaseModel


class Response(BaseModel):
    name: str
    email: str
    postedAt: datetime
    content: str
    id: str
