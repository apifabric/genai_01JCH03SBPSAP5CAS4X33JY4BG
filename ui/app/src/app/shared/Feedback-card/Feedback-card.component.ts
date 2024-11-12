import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Feedback-card.component.html',
  styleUrls: ['./Feedback-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Feedback-card]': 'true'
  }
})

export class FeedbackCardComponent {


}