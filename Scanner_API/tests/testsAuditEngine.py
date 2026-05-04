import pytest

def test_ping_scan_find_hosts():
    engine = AuditEngine()

    found_devices = engine.perform_ping_scan()

    assert isinstance(found_devices, list)

    assert len(found_devices) > 0

    assert hasattr(found_devices[0], "ip_address")
