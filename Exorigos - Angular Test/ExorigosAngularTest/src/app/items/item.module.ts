export class Item {
    public id: string;
    public description: string;
    public name: string;
    public price: number;

    constructor(id: string, name: string, desc: string, price: number) {
        this.id = id;
        this.name = name;
        this.description = desc;
        this.price = price;
    }
}