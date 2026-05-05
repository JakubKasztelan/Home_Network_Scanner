import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {DashboardComponent} from '../DashboardComponent/DashboardComponent';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, DashboardComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('network-scanner-frontend');
}
