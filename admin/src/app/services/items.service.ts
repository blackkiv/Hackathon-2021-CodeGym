import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";
import { ItemInterface } from "../types/item.type";
import { API_URL } from '../settings';

@Injectable()
export class ItemsService {
    constructor(private http: HttpClient) {}


    getItems(): Observable<ItemInterface[]> {
        return this.http.get<ItemInterface[]>(API_URL + 'items/')
    }

    deleteItem(item: ItemInterface) {
        return this.http.delete(API_URL + `items/?name=${item.name}&shopName=${item.shopName}`, { responseType: 'text' })
    }

}