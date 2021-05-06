package hackathon.hack.repository;

import hackathon.hack.entity.Item;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ItemRepository extends JpaRepository<Item, Long> {

    List<Item> findByName(String name);

//    Item findByNameAndStore
}
