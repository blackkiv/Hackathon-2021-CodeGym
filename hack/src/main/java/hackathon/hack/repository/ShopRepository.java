package hackathon.hack.repository;

import hackathon.hack.entity.Shop;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ShopRepository extends JpaRepository<Shop, Long> {

    Shop findByLongitudeAndLatitude(String longitude, String latitude);
}
