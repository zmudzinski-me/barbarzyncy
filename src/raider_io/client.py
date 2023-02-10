import logging
from typing import List

import requests
from requests.exceptions import HTTPError

from config import settings
from core.types import JSON
from progress.models import Progress
from progress.repositories import ProgressRepository


class RaiderIOClient:
    _PROGRESS = ProgressRepository.get_progress()

    @classmethod
    def get_progress(cls) -> List[JSON]:
        result = []

        try:
            response = requests.get(
                settings.RAIDER_IO_URL,
                params={
                    "region": settings.GUILD_REGION,
                    "realm": settings.GUILD_REALM,
                    "name": settings.GUILD_NAME,
                    "fields": "raid_progression",
                },
            )
            response.raise_for_status()

            raid_progression = response.json().get("raid_progression")
            for raid_name in raid_progression:
                try:
                    raid_progress = cls._PROGRESS.get(raid_key=raid_name)
                except Progress.DoesNotExist:
                    continue

                raid = raid_progression[raid_name]
                raid["name"] = raid_progress.raid_name
                raid["image"] = raid_progress.image.url
                result.append(raid)

        except HTTPError:
            logging.error("Could not retrieve progress from Raider.io", exc_info=True)
        finally:
            return result
