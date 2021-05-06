package hackathon.hack.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.ToString;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
@ToString
public class ItemRequestDto {

    private String name;
    private String shopName;
    private String longitude;
    private String latitude;
    private Double price;
    private String fileId;
}
