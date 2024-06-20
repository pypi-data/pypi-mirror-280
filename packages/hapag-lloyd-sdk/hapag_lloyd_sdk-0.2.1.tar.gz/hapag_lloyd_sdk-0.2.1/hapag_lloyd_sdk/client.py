import os
import requests
from typing import List, Optional, Dict, Any


class HapagLloydClient:
    def __init__(self, client_id: Optional[str] = None, client_secret: Optional[str] = None, base_url: str = "https://api.hlag.com/hlag/external/v2/events"):
        self.client_id = client_id or os.getenv("HAPAG_LLOYD_CLIENT_ID")
        self.client_secret = client_secret or os.getenv("HAPAG_LLOYD_CLIENT_SECRET")

        if not self.client_id or not self.client_secret:
            raise ValueError("Client ID and Client Secret must be provided either as arguments or environment variables.")

        self.base_url = base_url
        self.headers = {
            "X-IBM-Client-Id": self.client_id,
            "X-IBM-Client-Secret": self.client_secret,
        }

    def get_events(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

