from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from services.settings import SettingsService

router = APIRouter()
templates = Jinja2Templates(directory="pages")


@router.get("/", include_in_schema=False, response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "settings": SettingsService.settings},
    )
