import socket

from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
from models.device import DeviceProfile


class AuditEngine:
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

            devices = []
            for sent, received in result:
                devices.append(DeviceProfile(
                    ip_address=received.psrc,
                    device_name="Discovered Device"
                ))

            return devices

        except Exception as e:
            print(f"Scan Error: {e}")
            return []