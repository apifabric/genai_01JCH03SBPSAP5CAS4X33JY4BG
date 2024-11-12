import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Appointment-new',
  templateUrl: './Appointment-new.component.html',
  styleUrls: ['./Appointment-new.component.scss']
})
export class AppointmentNewComponent {
  @ViewChild("AppointmentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}