package hackathon.hack.controller;

import hackathon.hack.dto.GeoEncodedResponseDto;
import hackathon.hack.dto.LatLngRequestDto;
import hackathon.hack.service.GoogleMapsApi;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@CrossOrigin
@RestController
@RequestMapping(value = "")
public class GeoController {

    private final GoogleMapsApi googleMapsApi;

    @Autowired
    public GeoController(GoogleMapsApi googleMapsApi) {
        this.googleMapsApi = googleMapsApi;
    }

    @GetMapping("geo-encoding/")
    public ResponseEntity<GeoEncodedResponseDto> getGeoEncoding(@RequestBody LatLngRequestDto latlng) {
        String result = GoogleMapsApi.getAddress(latlng.getLatitude(), latlng.getLongitude());

        if (result.equals("САВВА, НЕ ОТПРАВЛЯЙ МОРЕ!!!")) {
            return ResponseEntity.badRequest().body(GeoEncodedResponseDto.fromString(result));
        }
        return ResponseEntity.ok(GeoEncodedResponseDto.fromString(result));
    }

    @GetMapping("geo-place/")
    public ResponseEntity<GeoEncodedResponseDto> getPlace(@RequestBody LatLngRequestDto latlng) {
        String result = GoogleMapsApi.getShopName(latlng.getLatitude(), latlng.getLongitude());

        if (result.equals("САВВА, НЕ ОТПРАВЛЯЙ МОРЕ!!!")) {
            return ResponseEntity.badRequest().body(GeoEncodedResponseDto.fromString(result));
        }
        return ResponseEntity.ok(GeoEncodedResponseDto.fromString(result));
    }


}
