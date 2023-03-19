import { ItemService } from './services/items.service';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ItemsComponent } from './items/items.component';
import { HttpClientModule } from '@angular/common/http';
import { DxDataGridModule, DxButtonModule } from 'devextreme-angular';
import { FormsModule } from '@angular/forms';
import { DxPopupModule } from 'devextreme-angular/ui/popup';
import { ItemAddFormComponent } from './items/item-add-form/item-add-form.component';


@NgModule({
  declarations: [
    AppComponent,
    ItemsComponent,
    ItemAddFormComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    HttpClientModule,
    DxDataGridModule,
    DxPopupModule,
    DxButtonModule ],
  providers: [ItemService],
  bootstrap: [AppComponent]
})
export class AppModule { }
