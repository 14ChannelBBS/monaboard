from pydantic import BaseModel, Field

from typing import Optional


class BoardSettings(BaseModel):
    bbsName: str = Field(..., alias="BBS_NAME")
    bbsNanasiName: str = Field(..., alias="BBS_NONAME_NAME")
    bbsDeletedName: str = Field(..., alias="BBS_DELETE_NAME")
    bbsLineNumber: int = Field(..., alias="BBS_LINE_NUMBER")
    bbsSubjectCount: int = Field(..., alias="BBS_SUBJECT_COUNT")
    bbsNameCount: int = Field(..., alias="BBS_NAME_COUNT")
    bbsMailCount: int = Field(..., alias="BBS_MAIL_COUNT")
    bbsMessageCount: int = Field(..., alias="BBS_MESSAGE_COUNT")
