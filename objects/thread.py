from datetime import datetime
from typing import List

from pydantic import BaseModel

from .response import Response


class Thread(BaseModel):
    subject: str
    createdAt: datetime
    responses: List[Response]
