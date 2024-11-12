import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Staff-card.component.html',
  styleUrls: ['./Staff-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Staff-card]': 'true'
  }
})

export class StaffCardComponent {


}