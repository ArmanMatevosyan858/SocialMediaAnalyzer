from models.BaseClass import BaseClass
from configurations import instagram
from properties.InstagramTypes import InstagramTypes
import requests


class Instagram(BaseClass):
    """
    Instagram Api Request Class
    """

    def __init__(self):
        """
        Initialization of the class
        """

        self.network_income_data = None

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

    def get_url(self, account_data_value, account_value):
        """
        The method is returning request final url
        :param account_data_value:
        :param account_value:
        :return:
        """

        return str(self.generate_url([
            InstagramTypes.ROOT_REQUEST.value,
            InstagramTypes.INSTAGRAM_VERSION.value,
            account_data_value,
            account_value,
            InstagramTypes.MEDIA_DATA.value,
            InstagramTypes.RECENT.value,
            str(InstagramTypes.ACCESS_TOKEN.value + instagram.TOKEN)
        ]))

    def get_media_data(self, account_data_value, account_value):
        """
        The method requests from instagram api data
        :param account_data_value:
        :param account_value:
        :return:
        """

        return requests.get(self.get_url(account_data_value, account_value))

    def get_personal_media(self):
        """
        The method returns api data of personal media
        :return:
        """

        response = self.get_media_data(InstagramTypes.USERS.value,
                                       InstagramTypes.PERSONAL_DATA.value)

        if response.status_code == 404:
            self.error("RESPONSE INVALID")
            self.error(self.get_url(InstagramTypes.USERS.value,
                                    InstagramTypes.PERSONAL_DATA.value))
            return None
        elif response.status_code == 200:
            return response.content
