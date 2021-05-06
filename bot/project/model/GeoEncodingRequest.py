class GeoEncodingRequest:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def json(self):
        return {
            "latitude": str(self.latitude),
            "longitude": str(self.longitude)
        }