package hackathon.hack.controller;

import hackathon.hack.dto.ItemDto;
import hackathon.hack.dto.ItemRequestDto;
import hackathon.hack.entity.Item;
import hackathon.hack.entity.Shop;
import hackathon.hack.service.ItemService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping(value = "/items/")
public class ItemController {

    private final ItemService itemService;

    public ItemController(ItemService itemService) {
        this.itemService = itemService;
    }

    @GetMapping(value = "/")
    public ResponseEntity findAll() {
        return ResponseEntity.ok(
            itemService.findAll().stream()
                    .map(ItemDto::fromItem)
                    .collect(Collectors.toList())
        );
    }

    @GetMapping(value = "/search/")
    public ResponseEntity findByNameLike(@RequestParam String name) {
        return ResponseEntity.ok(
            itemService.findByNameLike(name).stream()
                .map(ItemDto::fromItem)
                .collect(Collectors.toList())
        );
    }

    @PostMapping(value = "/")
    public ResponseEntity<ItemDto> save(@RequestBody ItemRequestDto requestDto) {
        Item item = new Item();
        item.setName(requestDto.getName());
        item.setPrice(requestDto.getPrice());
        item.setFileId(requestDto.getFileId());

        Shop shop = new Shop();
        shop.setName(requestDto.getShopName());
//        shop.setName("ATB");
        shop.setLatitude(requestDto.getLatitude());
        shop.setLongitude(requestDto.getLongitude());

        item.setShop(shop);

        return ResponseEntity.ok(
            ItemDto.fromItem(itemService.save(item))
        );
    }
}
