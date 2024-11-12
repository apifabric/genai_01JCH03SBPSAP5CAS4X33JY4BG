import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Feedback-new',
  templateUrl: './Feedback-new.component.html',
  styleUrls: ['./Feedback-new.component.scss']
})
export class FeedbackNewComponent {
  @ViewChild("FeedbackForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}