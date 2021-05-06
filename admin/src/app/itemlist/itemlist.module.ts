import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { ItemListComponent } from "./itemlist.component";

@NgModule({
    declarations: [ItemListComponent],
    imports: [CommonModule],
    exports: [ItemListComponent]
})

export class ItemListModule { }