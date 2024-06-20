from typing import List, Optional, Dict, Any
from .client import HapagLloydClient
from .models import Event, TransportEvent, ShipmentEvent, EquipmentEvent

def get_events(client: HapagLloydClient, params: Optional[Dict[str, Any]] = None) -> List[Event]:
    events_data = client.get_events(params)
    events = []
    for event_data in events_data:
        if event_data.get('eventType') == 'TRANSPORT':
            events.append(TransportEvent(**event_data))
        elif event_data.get('eventType') == 'SHIPMENT':
            events.append(ShipmentEvent(**event_data))
        elif event_data.get('eventType') == 'EQUIPMENT':
            events.append(EquipmentEvent(**event_data))
        else:
            events.append(Event(**event_data))
    return events
