import { Item } from './item.module';
import { Component, OnInit } from '@angular/core';
import { ItemService } from '../services/items.service';
import { v4 as uuid } from 'uuid';



@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css']
})
export class ItemsComponent implements OnInit{
  items: any = [];
  currentFilter:any;
  showAddingForm = false;
  selectedRows: string[] = [];
  focusedRowKey: string = '';

  autoNavigateToFocusedRow = true;

  constructor(private itemService: ItemService) { }

  ngOnInit() {
    // get items object from json file
    this.itemService.getItemsRequest()
      .subscribe( (items) => this.items = items);

    // subscribe to detect changes in items object
    this.itemService.itemsChanged.subscribe( (items) => this.items = items);
    this.focusedRowKey = this.items ? this.items[0].id : '';

  }

  openPopup(){
    this.showAddingForm = true;
  }

  // add new item from form detailt to items object
  addItem(item: { name: string; desc: string; price: number; }) {
    const newItem = new Item(uuid(), item.name, item.desc, item.price);
    this.itemService.addItem(newItem);

    this.showAddingForm = false;
    this.selectedRows = this.items.filter((itemEl: Item) => itemEl.id === newItem.id).map((itemEL: Item) => itemEL.id);
    this.focusedRowKey = this.selectedRows? this.selectedRows[0] : '';
  }


  updateRow(event: any) {
    this.itemService.updateItem(event.data);
  }

  removeRow(event: any) {
    this.itemService.deleteItem(event.data.id);
  }

}
