import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Event-card.component.html',
  styleUrls: ['./Event-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Event-card]': 'true'
  }
})

export class EventCardComponent {


}