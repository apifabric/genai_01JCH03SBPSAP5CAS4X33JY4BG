import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FeedbackHomeComponent } from './home/Feedback-home.component';
import { FeedbackNewComponent } from './new/Feedback-new.component';
import { FeedbackDetailComponent } from './detail/Feedback-detail.component';

const routes: Routes = [
  {path: '', component: FeedbackHomeComponent},
  { path: 'new', component: FeedbackNewComponent },
  { path: ':id', component: FeedbackDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Feedback-detail-permissions'
      }
    }
  }
];

export const FEEDBACK_MODULE_DECLARATIONS = [
    FeedbackHomeComponent,
    FeedbackNewComponent,
    FeedbackDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FeedbackRoutingModule { }