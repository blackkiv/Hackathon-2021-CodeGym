package hackathon.hack.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import hackathon.hack.entity.Item;
import hackathon.hack.service.GoogleMapsApi;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.ToString;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
@ToString
@AllArgsConstructor
public class ItemDto {

    private String name;
    private Double price;
    private String shopName;
    private String address;
    private String fileId;

    public static ItemDto fromItem(Item item) {
        ItemDto itemDto = new ItemDto(
                item.getName(),
                item.getPrice(),
                item.getShop().getName(),
                GoogleMapsApi.getAddress(item.getShop().getLatitude(), item.getShop().getLongitude()),
                item.getFileId()
        );

        return itemDto;
    }
}
