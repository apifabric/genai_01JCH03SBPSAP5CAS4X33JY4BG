import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AttendanceHomeComponent } from './home/Attendance-home.component';
import { AttendanceNewComponent } from './new/Attendance-new.component';
import { AttendanceDetailComponent } from './detail/Attendance-detail.component';

const routes: Routes = [
  {path: '', component: AttendanceHomeComponent},
  { path: 'new', component: AttendanceNewComponent },
  { path: ':id', component: AttendanceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Attendance-detail-permissions'
      }
    }
  }
];

export const ATTENDANCE_MODULE_DECLARATIONS = [
    AttendanceHomeComponent,
    AttendanceNewComponent,
    AttendanceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AttendanceRoutingModule { }