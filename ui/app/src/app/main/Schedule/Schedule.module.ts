import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SCHEDULE_MODULE_DECLARATIONS, ScheduleRoutingModule} from  './Schedule-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ScheduleRoutingModule
  ],
  declarations: SCHEDULE_MODULE_DECLARATIONS,
  exports: SCHEDULE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ScheduleModule { }