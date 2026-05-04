import os

from models.device import DeviceProfile


def test_pdf_report_creation():
    generator = ReportGenerator()
    devices = [DeviceProfile(ip_address="192.168.0.1", open_ports=[80])]

    path = generator.generate_technical_report(devices, score=90)

    assert os.path.exists(path)
    assert path.endswith(".pdf")

    if os.path.exists(path):
        os.remove(path)