import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StockHomeComponent } from './home/Stock-home.component';
import { StockNewComponent } from './new/Stock-new.component';
import { StockDetailComponent } from './detail/Stock-detail.component';

const routes: Routes = [
  {path: '', component: StockHomeComponent},
  { path: 'new', component: StockNewComponent },
  { path: ':id', component: StockDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Stock-detail-permissions'
      }
    }
  }
];

export const STOCK_MODULE_DECLARATIONS = [
    StockHomeComponent,
    StockNewComponent,
    StockDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StockRoutingModule { }