![License](https://img.shields.io/github/license/divinebanana/barbarzyncy)

# Barbarzyncy Website

The project contains Django code for the Barbarzyńcy World of Warcraft guild located on the Burning Legion server. This was created as a side project, when recruitment problems arose, so we wanted to create some marketing value for future guild players, while making the recruitment process more smooth for us.

## Features
  - News banners
  - Blog and news
  - `Raider.io` progress
  - Guild raiding / pvp groups
  - Recruitment connected with `Discord`
  - `BlizzardAPI` connection for character information

## Requirements
  * Python 3.9
  * [docker](https://docs.docker.com/docker-for-mac/install/)
  * [docker-compose](https://docs.docker.com/compose/install/)

## Environment Variables

| **Variable** | **Description** |
| :--- | :--- |
| `SECRET_KEY` | A secure key for the Django application |
| `ALLOWED_HOSTS` | Who you allow into your app eg. `*` for all |
| `GUILD_NAME` | Raider.io guild name |
| `GUILD_REALM` | Raider.io guild server |
| `GUILD_REGION` | Raider.io guild region |
| `RAIDER_IO_URL` | Raider.io API path |
| `WOW_CLIENT_ID` | Blizzard API client id |
| `WOW_CLIENT_SECRET` | Blizzard API secret |
| `DISCORD_CLIENT_ID` | Discord API client id |
| `DISCORD_CLIENT_SECRET` | Discord API secret |
| `DISCORD_URL` | Discord API path |
| `DISCORD_TOKEN` | Discord bot token |
| `DISCORD_GUILD_ID` | Discord guild server id |
| `DISCORD_CATEGORY_ID` | Category in which recruitment application should be created |

## Useful commands

| **Action** | **Command** |
| :--- | :--- |
| Build the project | `docker compose build` |
| Run the project | `docker compose up` |
| Format project | `docker compose run django fmt` |
| Lint project | `docker compose run django lint` |
