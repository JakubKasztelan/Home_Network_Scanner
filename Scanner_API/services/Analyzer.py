from models.device import DeviceProfile

class SecurityAnalyzer:
    def __init__(self):
        self.vulnerability_db = {
            21: {"label": "Unsecured File Cabinet (FTP)", "weight": 20},
            23: {"label": "Unlocked Front Door (Telnet)", "weight": 30},
            80: {"label": "Unprotected Web Service (HTTP)", "weight": 10},
            445: {"label": "Shared Storage Exposed (SMB)", "weight": 25}
        }

    def calculate_health_score(self, devices: list[DeviceProfile]) -> int:
        total_deduction = 0

        for device in devices:
            for port in device.open_ports:
                if port in self.vulnerability_db:
                    total_deduction += self.vulnerability_db[port]["weight"]

        return max(0, 100 - total_deduction)

    def translate_to_plain_english(self, port: int) -> str:
        return self.vulnerability_db.get(port, {}).get("label", "Unknown Vulnerability")