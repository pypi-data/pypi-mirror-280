from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class Event(BaseModel):
    eventCreatedDateTime: Optional[str] = None
    eventType: Optional[str] = None
    eventClassifierCode: Optional[str] = None
    eventDateTime: Optional[str] = None


class TransportEvent(Event):
    transportEventTypeCode: Optional[str] = None
    transportCallID: Optional[str] = None
    transportCall: Optional[Dict[str, Any]] = None


class ShipmentEvent(Event):
    shipmentEventTypeCode: Optional[str] = None
    documentID: Optional[str] = None
    documentTypeCode: Optional[str] = None


class EquipmentEvent(Event):
    equipmentEventTypeCode: Optional[str] = None
    equipmentReference: Optional[str] = None
    ISOEquipmentCode: Optional[str] = None
    emptyIndicatorCode: Optional[str] = None
    eventLocation: Optional[Dict[str, Any]] = None
    transportCallID: Optional[str] = None
    transportCall: Optional[Dict[str, Any]] = None
