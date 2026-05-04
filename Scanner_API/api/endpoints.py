from fastapi import APIRouter

from services.Analyzer import SecurityAnalyzer
from services.AuditEngine import AuditEngine

router = APIRouter()

@router.post("/audit/start")
async def start_audit():
    engine = AuditEngine()
    analyzer = SecurityAnalyzer()

    devices = engine.perform_ping_scan()

    for device in devices:
        device.open_ports = engine.scan_high_risk_ports(device.ip_address)

    health_score = analyzer.calculate_health_score(devices)

    return {
        "health_score": health_score,
        "devices": [
            {
                "ip": d.ip_address,
                "findings": [analyzer.translate_to_plain_english(p) for p in d.open_ports]
            } for d in devices
        ]
    }