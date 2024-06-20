import unittest
from hapag_lloyd_sdk.client import HapagLloydClient
from hapag_lloyd_sdk.api import get_events
from os import environ

CLIENT_ID = environ.get("CLIENT_ID")
CLIENT_SECRET = environ.get("CLIENT_SECRET")


class TestHapagLloydSDK(unittest.TestCase):
    def setUp(self):
        self.client = HapagLloydClient(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    def test_get_events_by_equipment_reference(self):
        params = {
            "eventType": "EQUIPMENT",
            "equipmentReference": "FBIU0503873",  # Example equipment reference
            "limit": 5
        }
        events = get_events(self.client, params)
        self.assertIsInstance(events, list)
        self.assertGreater(len(events), 0)
        for event in events:
            self.assertEqual(event.equipmentReference, "FBIU0503873")


if __name__ == '__main__':
    unittest.main()
