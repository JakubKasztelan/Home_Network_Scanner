from typing import Optional, List
from pydantic import BaseModel

class DeviceProfile(BaseModel):
    ip_address: str
    device_name: Optional[str] = "Unknown Device"
    operating_system: Optional[str] = "Unknown"
    open_ports: List[int] = []
    risk_level: str = "Low"
    findings: List[str] = []