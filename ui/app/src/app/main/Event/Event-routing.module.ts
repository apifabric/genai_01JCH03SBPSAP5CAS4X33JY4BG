import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EventHomeComponent } from './home/Event-home.component';
import { EventNewComponent } from './new/Event-new.component';
import { EventDetailComponent } from './detail/Event-detail.component';

const routes: Routes = [
  {path: '', component: EventHomeComponent},
  { path: 'new', component: EventNewComponent },
  { path: ':id', component: EventDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Event-detail-permissions'
      }
    }
  },{
    path: ':event_id/Attendance', loadChildren: () => import('../Attendance/Attendance.module').then(m => m.AttendanceModule),
    data: {
        oPermission: {
            permissionId: 'Attendance-detail-permissions'
        }
    }
}
];

export const EVENT_MODULE_DECLARATIONS = [
    EventHomeComponent,
    EventNewComponent,
    EventDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class EventRoutingModule { }