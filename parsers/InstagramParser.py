from models.InstagramPosts import InstagramPosts
import json
import xlsxwriter

class InstagramParser:

	"""
	Class to get Instagram API Data
	"""

	def __init__(self):
		self.user_list = []
		self.all_users = []
		self.excel_file_name = 'output.xlsx'
		self.path = '..\\SocialMediaAnalyzer\\output directory\\'
		self.array_likes = []

	def get_user_content(self, instagram_response_content):
		instaPosts = json.loads(instagram_response_content)
		for item in instaPosts['data']:
			self.user_list.append(item)
		for list_item in self.user_list:
			self.all_users.append(list_item)
		print(self.all_users)

		"""
		Loop over Json file of API 
		"""


	def check_if_key_exist(self, keys_hierarchy_list, dictionary):
		new_dictionary = dictionary
		for key in keys_hierarchy_list:
			if type((new_dictionary is dict)) and (key in new_dictionary):
				new_dictionary = new_dictionary[key]
			else:
				return False

		return True

	"""
	Checking if there is such keys in Data 
	"""

	def read_text_file(self):
		print('this are users', self.all_users)
		for data in self.all_users:
			url = None
			likes = None
			text = None
			if self.check_if_key_exist(['images', 'standard_resolution', 'url'], data):
				url = data['images']['standard_resolution']['url']
				print(url)
			if self.check_if_key_exist(['likes'], data):
				likes = data['likes']
			if self.check_if_key_exist(['caption', 'text'], data):
				text = data['caption']['text']

			self.array_likes.append(InstagramPosts(url=url, likes=likes, text=text))
			print(self.array_likes)

		"""
		Filter over Data  
		"""

	def main(self):
		self.read_text_file()

	"""
	Work all the Functions in a current Class 
	"""

