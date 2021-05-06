package hackathon.hack.service.impl;

import hackathon.hack.entity.Item;
import hackathon.hack.repository.ItemRepository;
import hackathon.hack.service.ItemService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@Slf4j
public class ItemServiceImpl implements ItemService {

    private final ItemRepository itemRepository;

    @Autowired
    public ItemServiceImpl(ItemRepository itemRepository) {
        this.itemRepository = itemRepository;
    }

    @Override
    public Item save(Item item) {
        Item savedItem = itemRepository.save(item);
        log.info("IN save - item: {} succesfully saved", savedItem);
        return savedItem;
    }

    @Override
    public List<Item> findAll() {
        List<Item> result = itemRepository.findAll();
        log.info("IN findAll - {} items found", result.size());
        return result;
    }

    @Override
    public List<Item> findByNameLike(String name) {
        List<Item> result = itemRepository.findByNameLike(name);
        log.info("IN findByNameLike - {} items found", result.size());
        return result;
    }

    @Override
    public Item update(Item item) {
//        Item itemDb = itemRepository.findById(item.getId())

        return null;
    }
}
