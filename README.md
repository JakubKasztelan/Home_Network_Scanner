# Home Network Scanner
The Home Network Scanner is an automated security auditing tool designed for home users to identify active devices on their network, scan for high-risk open ports and generate a technical report.  

## Project Specification
The full technical requirements, system architecture and design specifications for this project are documented in the SRS IEEE 830 (v5) document in the /SRS directory of this repository.  

## Features
- Device Discovery: Automatically identifies all active devices within the local subnet using ARP scanning.  
- Vulnerability Assessment: Scans devices for open ports and maps them to known security risks defined in a local database.  
- Health Scoring: Calculates an overall security score based on the severity of identified risks.  
- Technical Reporting: Generates a PDF report with the findings details for each device.  

## Tech Stack
- Backend: Python (FastAPI), Scapy for network analysis, and FPDF for report generation.  
- Frontend: Angular.  
- Data: JSON-based vulnerability database for port-to-finding mapping.  

## Installation and Setup
### Prerequisites
- Python 3.10+.  
- Node.js & npm.  
- Nmap/Npcap (Required for Scapy network interactions on some operating systems).  

### 1. Download the Repository
Clone the repository to your local machine:

`Bash
git clone https://github.com/jakubkasztelan/home_network_scanner.git
cd home_network_scanner
`

### 2. Backend Setup (Scanner_API)
Navigate to the API directory and install the required Python packages:  

`Bash
cd Scanner_API
pip install fastapi uvicorn scapy fpdf2
`

Run the backend server (Note: Sudo/Administrator privileges are required for Scapy to perform network scans):  

`Bash
sudo python main.py
`
The API will be available at http://localhost:8000.

### 3. Frontend Setup (network-scanner-frontend)
Navigate to the frontend directory and install the dependencies:  

`Bash
cd network-scanner-frontend
npm install
`
Start the Angular development server:

`Bash
npm start
`
The dashboard will be available at http://localhost:4200.

## How to Use
- Launch the Services: Ensure both the FastAPI backend and Angular frontend are running.  
- Access the Dashboard: Open your browser to http://localhost:4200.  
- Start Audit: Click the "Run Security Audit" button to begin the scan.  
- Review Results: View the overall Health Score and expand individual device cards to see specific IP addresses and security findings.  
- Export Report: Click "Download PDF Report" to save a detailed technical summary of the audit.  

## Directory Structure
- Scanner_API/: Contains the FastAPI implementation and network services.  
- network-scanner-frontend/: Contains the Angular source code (UI components).  
- SRS/: Contains the project specification document.
