package hackathon.hack.service;

import hackathon.hack.entity.Shop;

public interface ShopService {

    void save(Shop shop);

    Shop findByLongitudeAndLatitude(String longitude, String latitude);
}
