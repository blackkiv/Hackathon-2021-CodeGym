package hackathon.hack.service;

import hackathon.hack.utils.EncodeParams;
import hackathon.hack.utils.JsonReader;
import lombok.extern.slf4j.Slf4j;
import org.json.JSONObject;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Service
@Slf4j
public class GoogleMapsApi {
    private static final String API_URL_ENCODING = "https://maps.googleapis.com/maps/api/geocode/json";
    private static final String API_URL_STORE = "https://maps.googleapis.com/maps/api/place/autocomplete/json";

    public static String getAddress(String latitude, String longitude)  {
        Map<String, String> params = new HashMap<>();

        params.put("language", "en");
        params.put("sensor", "false");
        params.put("latlng", latitude + ',' + longitude);
        params.put("key", "AIzaSyDVXZdDaSSosyK7fSL6kIXwBoKLeIDSL1k");

        String url = API_URL_ENCODING + '?' + EncodeParams.encodeParams(params);
        JSONObject response = new JSONObject();
        try {
             response = JsonReader.read(url);
        } catch (IOException e) {
            e.printStackTrace();
        }

        JSONObject location = null;

        try {
            location = response.getJSONArray("results").getJSONObject(0);
        } catch (Exception ex) {
            return "САВВА, НЕ ОТПРАВЛЯЙ МОРЕ!!!";
        }
        String formattedAddress = location.getString("formatted_address");

        log.info("IN getAddress - address: {} got", formattedAddress);

        return formattedAddress;
    }

    public static String getShopName(String latitude, String longitude) {
        Map<String, String> params = new HashMap<>();

        params.put("input", "а");
        params.put("location", latitude + ',' + longitude);
        params.put("radius", "500");
        params.put("types", "store");
        params.put("key", "AIzaSyDVXZdDaSSosyK7fSL6kIXwBoKLeIDSL1k");

        String url = API_URL_STORE + '?' + EncodeParams.encodeParams(params);
        JSONObject response = new JSONObject();

        try {
            response = JsonReader.read(url);
        } catch (IOException e) {
            e.printStackTrace();
        }

        JSONObject location = null;

        try {
            location = response.getJSONArray("predictions").getJSONObject(0);
        } catch (Exception ex) {
            return ex.getMessage();
        }
        String description = location.getString("description");

        log.info("IN getShopName - shop name: {} got", description);

        return description;
    }

}
