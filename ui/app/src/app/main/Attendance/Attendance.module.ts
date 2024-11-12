import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ATTENDANCE_MODULE_DECLARATIONS, AttendanceRoutingModule} from  './Attendance-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AttendanceRoutingModule
  ],
  declarations: ATTENDANCE_MODULE_DECLARATIONS,
  exports: ATTENDANCE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AttendanceModule { }