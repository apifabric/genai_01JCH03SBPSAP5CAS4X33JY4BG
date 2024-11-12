import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Stock-card.component.html',
  styleUrls: ['./Stock-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Stock-card]': 'true'
  }
})

export class StockCardComponent {


}