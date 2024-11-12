import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Pet-card.component.html',
  styleUrls: ['./Pet-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Pet-card]': 'true'
  }
})

export class PetCardComponent {


}