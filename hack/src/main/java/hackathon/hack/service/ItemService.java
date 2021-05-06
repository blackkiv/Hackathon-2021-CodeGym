package hackathon.hack.service;

import hackathon.hack.entity.Item;

import java.util.List;

public interface ItemService {

    Item save(Item item);

    List<Item> findAll();

    Item update(Item item);

    void delete(String name, String shopName);
}
