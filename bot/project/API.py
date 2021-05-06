import requests

class API():

	base_url = "http://77.247.19.141:7896"
	
	address = f"{base_url}/geo-encoding/"
	add_item = f"{base_url}/items/"

	def __init__(self):
		pass

	def get_geo(self, data):
		return requests.get(self.address, json=data.json())

	def send_product(self, data):
		requests.post(self.add_item, json=data.json())

api = API()