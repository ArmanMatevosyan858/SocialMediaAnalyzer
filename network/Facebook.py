import requests
from models.BaseClass import BaseClass
from properties.FacebookTypes import FacebookTypes


class Facebook(FacebookTypes):
    """
	Instagram Api Request Class
	"""

    def __init__(self):
        """
		Initialization of the class
		"""

        self.network_income_data = None
        self.facebookApiRequest = FacebookTypes()

    @property
    def data(self):
        """
		Getter method
		:return: network_income_data
		"""

        return self.network_income_data

    @data.setter
    def data(self, value):
        """
		Setter class of the value
		:param value:
		:return:
		"""

        self.network_income_data = value

    def get_url(self):
        """
		The method is returning request final url
		:param account_data_value:
		:param account_value:
		:return:
		"""
        apiData = self.facebookApiRequest.request_to_facebook()
        print(apiData)
        return apiData
