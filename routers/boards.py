from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse

import aiofiles

from objects import BoardSettings

router = APIRouter()
templates = Jinja2Templates(directory="pages")


@router.get("/{boardName:str}/", include_in_schema=False)
async def boardIndex(request: Request, boardName: str):
    try:
        async with aiofiles.open(f"boards/{boardName}/settings.json") as f:
            bbsSettings = BoardSettings.model_validate_json(await f.read())
    except FileNotFoundError:
        raise HTTPException(404)


@router.get(
    "/{boardName:str}/SETTING.TXT",
    response_class=PlainTextResponse,
    include_in_schema=False,
)
async def boardSetting(request: Request, boardName: str):
    try:
        async with aiofiles.open(f"boards/{boardName}/settings.json") as f:
            bbsSettings = BoardSettings.model_validate_json(await f.read())
    except FileNotFoundError:
        raise HTTPException(404)

    data = bbsSettings.model_dump(by_alias=True)
    setting = ""
    for key, value in data.items():
        setting += f"{key}={value}\n"
    return setting
