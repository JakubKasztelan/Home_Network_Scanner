import pytest

from models.device import DeviceProfile
from services.Analyzer import SecurityAnalyzer


def test_security_score_calculation():
    analyzer = SecurityAnalyzer()

    perfect_device = DeviceProfile(ip_address="192.168.1.1", open_ports=[])
    assert analyzer.calculate_health_score([perfect_device]) == 100

    vulnerable_device = DeviceProfile(ip_address="192.168.1.5", open_ports=[23])
    score = analyzer.calculate_health_score([vulnerable_device])
    assert score < 100