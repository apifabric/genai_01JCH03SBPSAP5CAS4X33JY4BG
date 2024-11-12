import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {FEEDBACK_MODULE_DECLARATIONS, FeedbackRoutingModule} from  './Feedback-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    FeedbackRoutingModule
  ],
  declarations: FEEDBACK_MODULE_DECLARATIONS,
  exports: FEEDBACK_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class FeedbackModule { }