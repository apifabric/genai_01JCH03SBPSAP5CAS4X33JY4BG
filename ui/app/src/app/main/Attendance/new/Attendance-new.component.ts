import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Attendance-new',
  templateUrl: './Attendance-new.component.html',
  styleUrls: ['./Attendance-new.component.scss']
})
export class AttendanceNewComponent {
  @ViewChild("AttendanceForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}