from models.device import DeviceProfile
import json
import os

class SecurityAnalyzer:
    def __init__(self):
        base_path = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_path, "data", "ports.json")

        with open(db_path, "r") as f:
            self.vulnerability_db = json.load(f)

    def calculate_health_score(self, devices: list[DeviceProfile]) -> int:
        total_deduction = 0
        for device in devices:
            for port in device.open_ports:
                port_data = self.vulnerability_db.get(str(port))
                if port_data:
                    total_deduction += port_data["weight"]

        return max(0, 100 - total_deduction)

    def translate_to_plain_english(self, port: int) -> str:
        port_data = self.vulnerability_db.get(str(port))
        return port_data["label"] if port_data else f"Unknown Service (Port {port})"