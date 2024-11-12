import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PetHomeComponent } from './home/Pet-home.component';
import { PetNewComponent } from './new/Pet-new.component';
import { PetDetailComponent } from './detail/Pet-detail.component';

const routes: Routes = [
  {path: '', component: PetHomeComponent},
  { path: 'new', component: PetNewComponent },
  { path: ':id', component: PetDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Pet-detail-permissions'
      }
    }
  },{
    path: ':pet_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
},{
    path: ':pet_id/OrderItem', loadChildren: () => import('../OrderItem/OrderItem.module').then(m => m.OrderItemModule),
    data: {
        oPermission: {
            permissionId: 'OrderItem-detail-permissions'
        }
    }
},{
    path: ':pet_id/Stock', loadChildren: () => import('../Stock/Stock.module').then(m => m.StockModule),
    data: {
        oPermission: {
            permissionId: 'Stock-detail-permissions'
        }
    }
}
];

export const PET_MODULE_DECLARATIONS = [
    PetHomeComponent,
    PetNewComponent,
    PetDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PetRoutingModule { }