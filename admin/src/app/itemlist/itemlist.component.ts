import { Component, ɵSWITCH_COMPILE_PIPE__POST_R3__ } from "@angular/core";
import { ItemsService } from "../services/items.service";
import { ItemInterface } from "../types/item.type";

@Component({
    selector: 'app-items-list',
    templateUrl: './itemlist.component.html',
    styleUrls: ['./itemlist.component.scss']
})
export class ItemListComponent {
    constructor(private itemsService: ItemsService) {}

    items: ItemInterface[] = []

    refreshList() {
        this.itemsService.getItems().subscribe((res: ItemInterface[]) => {
			this.items = res
		});
    }

    deleteItem(item: ItemInterface) {
        this.itemsService.deleteItem(item).subscribe()

        this.items = this.items.filter((i) => i !== item);
    }

    ngOnInit() {
        this.refreshList();
    }
}