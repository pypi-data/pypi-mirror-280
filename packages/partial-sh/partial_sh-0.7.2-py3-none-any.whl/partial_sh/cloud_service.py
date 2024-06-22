import logging

import requests

logger = logging.getLogger(__name__)


class CloudService:
    # api_url: str = "http://localhost:8080"
    # webapp_url: str = "http://localhost:5173"
    api_url: str = "https://api.partial.sh"
    webapp_url: str = "https://console.partial.sh"

    def __init__(self):
        pass

    def list_workspaces(self, access_token: str):
        url = f"{self.api_url}/app/workspaces"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def create_sahper(self, access_token: str, workspace_id: str, shaper: dict):
        url = f"{self.api_url}/app/workspaces/{workspace_id}/shapers"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        response = requests.post(url, headers=headers, json=shaper)
        response.raise_for_status()
        return response.json()
