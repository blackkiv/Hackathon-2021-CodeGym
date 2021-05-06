package hackathon.hack.entity;

import lombok.Data;
import lombok.ToString;

import javax.persistence.*;

@Entity
@Data
@ToString
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String name;
    private Double price;
    @OneToOne(cascade = {CascadeType.ALL})
    private Shop shop;
    private String fileId;
}
