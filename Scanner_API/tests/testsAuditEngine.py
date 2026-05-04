import pytest

from services.AuditEngine import AuditEngine

def test_ping_scan_find_hosts():
    engine = AuditEngine()

    found_devices = engine.perform_ping_scan()

    print(found_devices)

    assert isinstance(found_devices, list)

    assert len(found_devices) > 0

    assert hasattr(found_devices[0], "ip_address")

def test_port_scan_identifies_open_ports():
    engine = AuditEngine()

    found_devices = engine.perform_ping_scan()

    if not found_devices:
        pytest.fail("No devices found to perform port scan test.")

    target_ip = found_devices[0].ip_address
    open_ports = engine.scan_high_risk_ports(target_ip)

    assert isinstance(open_ports, list)