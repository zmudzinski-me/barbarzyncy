import json
import logging
from typing import List, Tuple

from django.conf import settings
from django.db.models import QuerySet

import requests
from requests import HTTPError

from core.types import JSON
from recruitment.repositories import RecruitmentRepository


class DiscordClient:
    _CREATE_CHANNEL_URL = "/guilds/{guild_id}/channels"
    _SEND_MESSAGE_URL = "/channels/{channel_id}/messages"
    _AUTH_URL = (
        "https://discord.com/oauth2/authorize"
        "?response_type=code"
        "&client_id={client_id}"
        "&scope=identify%20guilds.join"
        "&redirect_uri=https://barbarzyncy.pl/rekrutacja/"
        "&prompt=consent"
    )
    _TOKEN_URL = "/oauth2/token"
    _ME_URL = "/users/@me"
    _GUILD_JOIN_URL = "/guilds/{guild_id}/members/{user_id}"
    _PERMISSIONS_URL = "/channels/{channel_id}/permissions/{user_id}"

    @classmethod
    def get_auth_link(cls) -> str:
        return cls._AUTH_URL.format(client_id=settings.DISCORD_CLIENT_ID)

    @classmethod
    def send_quesionnaire(
        cls,
        questions: QuerySet,
        answers: JSON,
        recruitment_type: str,
        token_type: str,
        access_token: str,
    ) -> None:
        try:
            token = f"{token_type} {access_token}"
            user_id, user_name = cls._get_user_details(token=token)

            RecruitmentRepository.check_questionnaire_exists(discord=user_name)

            channel_id = cls._create_channel(channel_name=user_name)
            cls._join_guild(user_id=user_id, token=access_token)
            cls._add_user_to_channel(user_id=user_id, channel_id=channel_id)

            cls._send_message(
                channel_id=channel_id,
                questions=questions,
                answers=answers,
                recruitment_type=recruitment_type,
                user_name=user_name,
            )

            RecruitmentRepository.save(discord=user_name)
        except HTTPError:
            logging.error("Discord Error", exc_info=True)
            raise ValueError(
                (
                    "Nie mogliśmy skontaktować się z serwerami Discord. "
                    "Spróbuj ponownie za jakiś czas."
                )
            )

    @classmethod
    def _create_channel(cls, channel_name: str) -> int:
        data = {
            "name": channel_name.replace("#", "-"),
            "parent_id": settings.DISCORD_CATEGORY_ID,
        }
        response = requests.post(
            url=settings.DISCORD_URL
            + cls._CREATE_CHANNEL_URL.format(guild_id=settings.DISCORD_GUILD_ID),
            data=json.dumps(data),
            headers={
                "Authorization": "Bot " + settings.DISCORD_TOKEN,
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()
        return response.json()["id"]

    @classmethod
    def _send_message(
        cls,
        channel_id: int,
        questions: QuerySet,
        answers: JSON,
        recruitment_type: str,
        user_name: str,
    ) -> None:
        embed = {
            "title": f"Rekrutacja {recruitment_type.upper()}",
            "description": f"**Użytkownik:** {user_name}",
        }

        fields: List[JSON] = []
        for question in questions:
            fields.append(
                {
                    "name": question.content,
                    "value": answers[question.id],
                }
            )
        embed["fields"] = fields  # type: ignore

        response = requests.post(
            url=settings.DISCORD_URL
            + cls._SEND_MESSAGE_URL.format(channel_id=channel_id),
            data=json.dumps({"embeds": [embed]}),
            headers={
                "Authorization": "Bot " + settings.DISCORD_TOKEN,
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()

    @classmethod
    def exchange_token(cls, code: str) -> Tuple[str, str]:
        data = {
            "client_id": settings.DISCORD_CLIENT_ID,
            "client_secret": settings.DISCORD_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "https://barbarzyncy.pl/rekrutacja/",
        }
        response = requests.post(
            url=settings.DISCORD_URL + cls._TOKEN_URL,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        response.raise_for_status()
        response_json = response.json()

        token_type = response_json["token_type"]
        access_token = response_json["access_token"]
        return token_type, access_token

    @classmethod
    def _get_user_details(cls, token: str) -> Tuple[int, str]:
        response = requests.get(
            url=settings.DISCORD_URL + cls._ME_URL, headers={"Authorization": token}
        )
        response.raise_for_status()
        response_json = response.json()

        user_id = response_json["id"]
        user_name = f"{response_json['username']}#{response_json['discriminator']}"
        return user_id, user_name

    @classmethod
    def _join_guild(cls, user_id: int, token: str) -> None:
        data = {"access_token": token}
        response = requests.put(
            url=settings.DISCORD_URL
            + cls._GUILD_JOIN_URL.format(
                guild_id=settings.DISCORD_GUILD_ID,
                user_id=user_id,
            ),
            data=json.dumps(data),
            headers={
                "Authorization": f"Bot {settings.DISCORD_TOKEN}",
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()

    @classmethod
    def _add_user_to_channel(cls, user_id: int, channel_id: int) -> None:
        data = {
            "allow": "68608",  # View Channel, Read History and Write Messages
            "type": 1,
        }
        response = requests.put(
            url=settings.DISCORD_URL
            + cls._PERMISSIONS_URL.format(
                channel_id=channel_id,
                user_id=user_id,
            ),
            data=json.dumps(data),
            headers={
                "Authorization": f"Bot {settings.DISCORD_TOKEN}",
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()
