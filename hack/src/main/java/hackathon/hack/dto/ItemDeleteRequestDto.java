package hackathon.hack.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.ToString;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
@ToString
public class ItemDeleteRequestDto {

    private String name;
    private String shopName;
}
