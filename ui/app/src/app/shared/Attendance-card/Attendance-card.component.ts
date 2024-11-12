import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Attendance-card.component.html',
  styleUrls: ['./Attendance-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Attendance-card]': 'true'
  }
})

export class AttendanceCardComponent {


}