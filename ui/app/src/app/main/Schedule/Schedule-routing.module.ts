import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ScheduleHomeComponent } from './home/Schedule-home.component';
import { ScheduleNewComponent } from './new/Schedule-new.component';
import { ScheduleDetailComponent } from './detail/Schedule-detail.component';

const routes: Routes = [
  {path: '', component: ScheduleHomeComponent},
  { path: 'new', component: ScheduleNewComponent },
  { path: ':id', component: ScheduleDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Schedule-detail-permissions'
      }
    }
  }
];

export const SCHEDULE_MODULE_DECLARATIONS = [
    ScheduleHomeComponent,
    ScheduleNewComponent,
    ScheduleDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ScheduleRoutingModule { }