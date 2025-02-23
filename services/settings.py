import aiofiles

from objects import Settings


class SettingsService:
    settings: Settings

    @classmethod
    async def load(cls):
        async with aiofiles.open("settings.json") as f:
            cls.settings = Settings.model_validate_json(await f.read())
