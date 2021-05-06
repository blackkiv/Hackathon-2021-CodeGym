package hackathon.hack.service.impl;

import hackathon.hack.entity.Shop;
import hackathon.hack.repository.ShopRepository;
import hackathon.hack.service.ShopService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class ShopServiceImpl implements ShopService {

    private final ShopRepository shopRepository;

    @Autowired
    public ShopServiceImpl(ShopRepository shopRepository) {
        this.shopRepository = shopRepository;
    }

    @Override
    public void save(Shop shop) {
        Shop savedShop = shopRepository.save(shop);
        log.info("IN save - shop: {} successfully saved", savedShop);
    }

    @Override
    public Shop findByLongitudeAndLatitude(String longitude, String latitude) {
        Shop result = shopRepository.findByLongitudeAndLatitude(longitude, latitude);
        log.info("IN save - findByLongitudeAndLatitude: {} found", result);
        return result;
    }
}
