import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Schedule-card.component.html',
  styleUrls: ['./Schedule-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Schedule-card]': 'true'
  }
})

export class ScheduleCardComponent {


}