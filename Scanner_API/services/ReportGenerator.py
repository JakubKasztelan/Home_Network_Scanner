from fpdf import FPDF
from datetime import datetime

class ReportGenerator:
    def generate_technical_report(self, devices, health_score):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("helvetica", "B", 16)
        pdf.cell(0, 10, "Home Network Security Health-Check Report", ln=True, align="C")

        pdf.set_font("helvetica", "", 12)
        pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
        pdf.set_font("helvetica", "B", 12)
        pdf.cell(0, 10, f"Overall Security Score: {health_score}/100", ln=True)
        pdf.ln(10)

        pdf.set_font("helvetica", "B", 14)
        pdf.cell(0, 10, "Discovered Devices & Risks:", ln=True)

        pdf.set_font("helvetica", "", 11)
        for device in devices:
            status = "ATTENTION REQUIRED" if device.get("findings") else "SECURE"
            pdf.set_font("helvetica", "B", 11)
            pdf.cell(0, 10, f"IP: {device['ip']} | Status: {status}", ln=True)

            pdf.set_font("helvetica", "", 11)
            # Loop through findings dynamically
            for finding in device.get("findings", []):
                pdf.cell(0, 8, f"  > Risk Detected: {finding}", ln=True)
            pdf.ln(2)

        file_path = "Security_Report.pdf"
        pdf.output(file_path)
        return file_path