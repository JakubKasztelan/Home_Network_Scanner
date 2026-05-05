import { Component, ChangeDetectorRef } from '@angular/core';
import { AuditService } from '../service/audit.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './DashboardComponent.html',
  styleUrl: './DashboardComponent.css',
})
export class DashboardComponent {
  healthScore: number = 100;
  devices: any[] = [];
  isScanning: boolean = false;

  constructor(private auditService: AuditService, private cdr: ChangeDetectorRef) {}

  runScan() {
    this.isScanning = true;
    this.auditService.startAudit().subscribe({
      next: (result) => {
        this.healthScore = result.health_score;

        this.devices = result.devices.map((device: any) => ({
          ...device,
          expanded: false
        }));

        this.isScanning = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Scan failed:', err);
        this.isScanning = false;
        this.cdr.detectChanges();
      }
    });
  }

  toggleDevice(device: any) {
    device.expanded = !device.expanded;
    this.cdr.detectChanges();
  }

  downloadReport() {
    const reportData = {
      health_score: this.healthScore,
      devices: this.devices
    };

    this.auditService.downloadReport(reportData).subscribe({
      next: (blob: Blob) => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `Home_Security_Report.pdf`;
        a.click();
        window.URL.revokeObjectURL(url);
      }
    });
  }
}
