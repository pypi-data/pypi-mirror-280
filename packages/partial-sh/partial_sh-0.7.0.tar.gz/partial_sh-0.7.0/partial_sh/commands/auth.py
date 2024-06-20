# Use refresh token to get a new access token

import logging
import time

import jwt
import requests
import typer

from ..auth_config import AuthConfig

logger = logging.getLogger(__name__)


def call_refresh_token_api(auth_url: str, refresh_token: str):
    # API call to refresh token
    # POST /auth/refresh-token

    res = requests.post(
        f"{auth_url}/auth/refresh",
        headers={
            "Content-Type": "application/json",
        },
        json={"refreshToken": refresh_token},
    )

    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        logger.error(e.response.text)
        return None

    data = res.json()

    return {
        "access_token": data.get("accessToken"),
        "refresh_token": data.get("refreshToken"),
    }


def is_access_token_expired(access_token: str):
    # Check if access token is expired
    # If expired, return True
    # Otherwise, return False
    res = jwt.decode(access_token, options={"verify_signature": False})
    exp = res.get("exp")
    # Check if access token is expired, exp is in seconds since epoch UNIX
    if exp:
        return exp < time.time()
    return False


def refresh_access_token(auth_url: str, auth_config: AuthConfig):
    # Check if access token is expired
    # If expired, use refresh token to get a new access token

    if not auth_config.access_token:
        logger.debug("No access token found. Please login first.")
        return None

    if not auth_config.refresh_token:
        logger.debug("No refresh token found. Please login first.")
        return None

    if not is_access_token_expired(auth_config.access_token):
        logger.debug("Access token is not expired.")
        return None

    logger.debug("Access token is expired. Refreshing access token...")

    # API call to refresh access token
    new_tokens = call_refresh_token_api(
        auth_url=auth_url, refresh_token=auth_config.refresh_token
    )

    if not new_tokens:
        logger.error("Failed to refresh access token.")
        return None

    auth_config.set_tokens(new_tokens["access_token"], new_tokens["refresh_token"])

    logger.debug("Access token refreshed.")


def get_access_token(ctx):
    auth_config = ctx.obj.get("auth")
    if not auth_config.access_token:
        print("No access token found. Please login first.")
        raise typer.Abort()
    auth_url = ctx.obj["cloud_service"].webapp_url
    refresh_access_token(auth_url=auth_url, auth_config=auth_config)
    return auth_config.access_token
