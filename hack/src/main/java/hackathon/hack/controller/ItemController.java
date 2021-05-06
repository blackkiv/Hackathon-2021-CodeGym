package hackathon.hack.controller;

import hackathon.hack.dto.ItemDeleteRequestDto;
import hackathon.hack.dto.ItemDto;
import hackathon.hack.dto.ItemRequestDto;
import hackathon.hack.entity.Item;
import hackathon.hack.entity.Shop;
import hackathon.hack.service.ItemService;
import hackathon.hack.service.ShopService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Comparator;
import java.util.Optional;
import java.util.stream.Collectors;

@CrossOrigin
@RestController
@RequestMapping(value = "/items/")
public class ItemController {

    private final ItemService itemService;
    private final ShopService shopService;

    @Autowired
    public ItemController(ItemService itemService, ShopService shopService) {
        this.itemService = itemService;
        this.shopService = shopService;
    }

    @GetMapping(value = "/")
    public ResponseEntity findAll(
            @RequestParam(required = false) Optional<String> name,
            @RequestParam(required = false) Optional<Double> maxPrice,
            @RequestParam(required = false) Optional<Double> minPrice
    ) {
        return ResponseEntity.ok(
            itemService.findAll().stream()
                .filter(item -> item.getName().toUpperCase().contains(name.orElse("").toUpperCase())
                    && item.getPrice() <= maxPrice.orElse(Double.MAX_VALUE)
                    && item.getPrice() >= minPrice.orElse(Double.MIN_VALUE))
                .map(ItemDto::fromItem)
                .sorted(Comparator.comparing(ItemDto::getPrice))
                .collect(Collectors.toList())
        );
    }

    @PostMapping(value = "/")
    public ResponseEntity<ItemDto> save(@RequestBody ItemRequestDto requestDto) {
        Item item = new Item();
        item.setName(requestDto.getName());
        item.setPrice(requestDto.getPrice());
        item.setFileId(requestDto.getFileId());

        Shop shop = shopService.findByLongitudeAndLatitude(requestDto.getLongitude(), requestDto.getLatitude());

        if (shop == null) {
            shop = new Shop();
            shop.setName(requestDto.getShopName());
            shop.setLatitude(requestDto.getLatitude());
            shop.setLongitude(requestDto.getLongitude());

            shopService.save(shop);
        }

        item.setShop(shop);

        return ResponseEntity.ok(
            ItemDto.fromItem(itemService.save(item))
        );
    }

    @DeleteMapping(value = "/")
    public ResponseEntity<String> delete(@RequestParam String name,
                                         @RequestParam String shopName) {
        itemService.delete(
                name, shopName
        );
        return ResponseEntity.ok("deleted");
    }
}
