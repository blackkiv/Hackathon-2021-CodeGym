class Item:
	def __init__(
		self, 
		idx: int, 
		shop_id: int, 
		photo_id: str,
		title: str,
		price: float
	):
	self.idx = idx
	self.shop_id = shop_id
	self.photo_id = photo_id
	self.title = title
	self.price = price