import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {APPOINTMENT_MODULE_DECLARATIONS, AppointmentRoutingModule} from  './Appointment-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AppointmentRoutingModule
  ],
  declarations: APPOINTMENT_MODULE_DECLARATIONS,
  exports: APPOINTMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppointmentModule { }