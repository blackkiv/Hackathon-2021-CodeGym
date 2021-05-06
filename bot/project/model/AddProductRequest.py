class AddProductRequest:

	def __init__(self, name: str, price: float, latitude: str, longitude: str):
		self.name = name
		self.shop_name = "" # placeholder
		self.price = price
		self.latitude = latitude
		self.longitude = longitude
		self.file_id = "" # placeholder

	def json(self):
		return {
			"name": self.name,
			"shopName": self.shop_name,
			"price": self.price,
			"latitude": self.latitude,
			"longitude": self.longitude,
			"fileId": self.file_id
		}