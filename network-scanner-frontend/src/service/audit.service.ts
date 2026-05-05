import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuditService {
  private apiUrl = "http://127.0.0.1:8000/api"

  constructor(private http: HttpClient) { }

  startAudit(): Observable<any> {
    return this.http.post(`${this.apiUrl}/audit/start`, {});
  }

  downloadReport(data: any): Observable<Blob> {
    return this.http.post(`${this.apiUrl}/audit/report`, data, { responseType: 'blob' });
  }
}

