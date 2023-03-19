import { EventEmitter, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Item } from '../items/item.module';


@Injectable()
export class ItemService {


  private itemsUrl = 'assets/data.json';

  private items: any = [];


  itemsChanged = new EventEmitter<Item[]>();


  constructor(private http: HttpClient) { 
    this.getItemsRequest()
      .subscribe( (items) => this.items = items);
  }


  getItemsRequest() {
    //get data from json file
    return this.http.get(this.itemsUrl);
  }


  addItem(item: Item) {
    this.items.push(item);
    this.itemsChanged.emit(this.items);
  }

  deleteItem(id: string) {
    this.items = this.items.filter((item: Item) => item.id != id);
    this.itemsChanged.emit(this.items);
  }

  updateItem(item: Item) {
    this.items = this.items.map((currItem: Item) =>
    currItem.id === item.id ? item : currItem
  );
    this.itemsChanged.emit(this.items);
  }

}
