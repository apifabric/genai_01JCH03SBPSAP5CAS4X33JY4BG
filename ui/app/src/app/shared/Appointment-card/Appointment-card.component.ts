import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Appointment-card.component.html',
  styleUrls: ['./Appointment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Appointment-card]': 'true'
  }
})

export class AppointmentCardComponent {


}