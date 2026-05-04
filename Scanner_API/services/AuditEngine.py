import os
import socket
import json
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp, sr1

from models.device import DeviceProfile


class AuditEngine:
    def __init__(self):
        base_path = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_path, "data", "ports.json")
        with open(db_path, "r") as f:
            self.target_ports = [int(p) for p in json.load(f).keys()]

    def perform_ping_scan(self) -> list[DeviceProfile]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()

            subnet = ".".join(local_ip.split('.')[:-1]) + ".0/24"
            print(f"\n[DEBUG] Scanning subnet: {subnet}")

            arp = ARP(pdst=subnet)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp

            result = srp(packet, timeout=2, verbose=False)[0]

            devices = [DeviceProfile(
                ip_address=local_ip,
                device_name="This Computer (Host)"
            )]

            for sent, received in result:
                devices.append(DeviceProfile(
                    ip_address=received.psrc,
                    device_name="Discovered Device"
                ))

            return devices

        except Exception as e:
            print(f"Scan Error: {e}")
            return []

    def scan_high_risk_ports(self, ip: str) -> list[int]:
        open_ports = []
        for port in self.target_ports:
            packet = IP(dst=ip) / TCP(dport=port, flags="S")
            response = sr1(packet, timeout=0.5, verbose=0)

            if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                open_ports.append(port)
        return open_ports