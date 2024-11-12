import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppointmentHomeComponent } from './home/Appointment-home.component';
import { AppointmentNewComponent } from './new/Appointment-new.component';
import { AppointmentDetailComponent } from './detail/Appointment-detail.component';

const routes: Routes = [
  {path: '', component: AppointmentHomeComponent},
  { path: 'new', component: AppointmentNewComponent },
  { path: ':id', component: AppointmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Appointment-detail-permissions'
      }
    }
  }
];

export const APPOINTMENT_MODULE_DECLARATIONS = [
    AppointmentHomeComponent,
    AppointmentNewComponent,
    AppointmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AppointmentRoutingModule { }