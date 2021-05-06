package hackathon.hack.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.ToString;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
@ToString
@AllArgsConstructor
public class GeoEncodedResponseDto {
    private String address;

    public static GeoEncodedResponseDto fromString(String address) {
        GeoEncodedResponseDto geoEncodedResponseDto = new GeoEncodedResponseDto(address);

        return geoEncodedResponseDto;
    }
}
