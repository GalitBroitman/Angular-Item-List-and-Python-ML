import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-item-add-form',
  templateUrl: './item-add-form.component.html',
  styleUrls: ['./item-add-form.component.css']
})
export class ItemAddFormComponent {
  name: string  = '';
  description: string = '';
  price: number = 0;


   @Input() popupVisible = false;

   @Output() popUpClosed = new EventEmitter<void>();
   @Output() submitForm = new EventEmitter();




  submit() {
    // emit the data of the form to the parent component
    if(this.name != '' && this.description != ''){
      this.submitForm.emit({name: this.name, desc: this.description,price:this.price});
      this.clearForm();
    }
    else {
      alert('Fill all Fields');
    }

  }

  cancel() {
    this.popUpClosed.emit();
    this.clearForm();
  }

  clearForm() {
    this.name ='';
    this.description ='';
    this.price = 0;
  }
 

}
