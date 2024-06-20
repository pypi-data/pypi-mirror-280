import requests
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class HapagLloydClient:
    def __init__(self, client_id: str, client_secret: str, base_url: str = "https://api.hlag.com/hlag/external/v2/events"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.headers = {
            "X-IBM-Client-Id": self.client_id,
            "X-IBM-Client-Secret": self.client_secret,
        }

    def get_events(self, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
