from fastapi import APIRouter
from starlette.responses import FileResponse

from services.Analyzer import SecurityAnalyzer
from services.AuditEngine import AuditEngine
from services.ReportGenerator import ReportGenerator

router = APIRouter()


@router.post("/api/audit/start")
async def start_audit():
    engine = AuditEngine()
    analyzer = SecurityAnalyzer()

    devices = engine.perform_ping_scan()
    for device in devices:
        device.open_ports = engine.scan_high_risk_ports(device.ip_address)

        device.findings = [analyzer.translate_to_plain_english(p) for p in device.open_ports]

    health_score = analyzer.calculate_health_score(devices)

    return {"health_score": health_score, "devices": devices}

@router.post("/audit/report")
async def create_report(audit_data: dict):
    generator = ReportGenerator()

    path = generator.generate_technical_report(
        devices=audit_data["devices"],
        health_score=audit_data["health_score"]
    )

    return FileResponse(path, filename="Home_Network_Report.pdf")