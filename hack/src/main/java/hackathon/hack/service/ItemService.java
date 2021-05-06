package hackathon.hack.service;

import hackathon.hack.entity.Item;

import java.util.List;

public interface ItemService {

    Item save(Item item);

    List<Item> findAll();

    List<Item> findByNameLike(String name);

    Item update(Item item);
}
