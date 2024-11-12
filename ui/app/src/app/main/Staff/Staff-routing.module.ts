import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StaffHomeComponent } from './home/Staff-home.component';
import { StaffNewComponent } from './new/Staff-new.component';
import { StaffDetailComponent } from './detail/Staff-detail.component';

const routes: Routes = [
  {path: '', component: StaffHomeComponent},
  { path: 'new', component: StaffNewComponent },
  { path: ':id', component: StaffDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Staff-detail-permissions'
      }
    }
  },{
    path: ':staff_id/Feedback', loadChildren: () => import('../Feedback/Feedback.module').then(m => m.FeedbackModule),
    data: {
        oPermission: {
            permissionId: 'Feedback-detail-permissions'
        }
    }
},{
    path: ':staff_id/Schedule', loadChildren: () => import('../Schedule/Schedule.module').then(m => m.ScheduleModule),
    data: {
        oPermission: {
            permissionId: 'Schedule-detail-permissions'
        }
    }
}
];

export const STAFF_MODULE_DECLARATIONS = [
    StaffHomeComponent,
    StaffNewComponent,
    StaffDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StaffRoutingModule { }