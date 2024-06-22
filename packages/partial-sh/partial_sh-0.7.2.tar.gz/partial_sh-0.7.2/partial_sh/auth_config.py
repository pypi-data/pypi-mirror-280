import json
from pathlib import Path
from typing import Optional


class AuthConfig:
    path: Path
    user: str = None
    access_token: str = None
    refresh_token: str = None

    def __init__(self, path: Path):
        self.path = path

    def set_auth(self, auth: dict):
        self.user = auth.get("user")
        self.access_token = auth.get("accessToken")
        self.refresh_token = auth.get("refreshToken")
        self.save()

    def set_tokens(self, access_token: str, refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.save()

    def save(self):
        # Convert the class attributes into a dictionary, ignoring None values
        data = {
            "user": self.user,
            "accessToken": self.access_token,
            "refreshToken": self.refresh_token,
        }
        # Filter out None values
        data = {key: value for key, value in data.items() if value is not None}
        # Save the dictionary as a JSON file at the specified path
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)
        return self

    def load(self):
        # Load data from the JSON file at the specified path
        # check if the file exists
        if not self.path.exists():
            return self
        with open(self.path, "r") as f:
            data = json.load(f)
        # Set the attributes of the class based on the loaded data
        self.user = data.get("user")
        self.access_token = data.get("accessToken")
        self.refresh_token = data.get("refreshToken")
        return self

    def clear(self):
        # Clear the attributes of the class
        self.user = None
        self.access_token = None
        self.refresh_token = None
        # Save the cleared data
        self.save()
        return self
