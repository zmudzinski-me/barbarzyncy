import logging
from typing import Optional

import requests
from requests.exceptions import HTTPError

from config import settings


class BattleNetClient:
    _AUTH_URL = "https://eu.battle.net/oauth/token"
    _MEDIA_URL = "https://eu.api.blizzard.com/profile/wow/character/{server}/{character_name}/character-media"  # noqa

    @classmethod
    def get_character_avatar(cls, name: str, server: str) -> Optional[str]:
        avatar = None
        try:
            token = cls._get_api_token()
            response = requests.get(
                cls._MEDIA_URL.format(
                    server=server,
                    character_name=name,
                ),
                params={
                    "namespace": "profile-eu",
                    "locale": "en_US",
                    "access_token": token,
                },
            )
            response.raise_for_status()

            assets = response.json()["assets"]
            for asset in assets:
                if asset.get("key") == "avatar":
                    avatar = asset.get("value")
        except (HTTPError, KeyError):
            logging.error("Could not gather avatar for character from Blizzard API.")
        finally:
            return avatar

    @classmethod
    def _get_api_token(cls) -> Optional[str]:
        response = requests.post(
            cls._AUTH_URL,
            data={"grant_type": "client_credentials"},
            auth=(settings.WOW_CLIENT_ID, settings.WOW_CLIENT_SECRET),
        )
        response.raise_for_status()

        return response.json().get("access_token")
