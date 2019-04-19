from models.BaseClass import BaseClass
from network.Instagram import Instagram
from parsers.InstagramParser import InstagramParser
from output.InstagramExcel import InstagramExcel
from network.Facebook import Facebook
from parsers.FacebookParser import FacebookParser
from output.FacebookExcel import FacebookExcel


class SocialMediaAnalyzer(BaseClass):
    """
    Main class
    """

    def __init__(self):
        """
        Initialization of the class
        """

        self.instagramApi = Instagram()
        self.facebookApi = Facebook()
        self.InstagramExcel = InstagramExcel()
        self.instagramParser = InstagramParser()
        self.facebookParser = FacebookParser()
        self.facebookExcel = FacebookExcel()

    def main(self):
        """
        Main method of the class
        :return:
        """
        facebook_response_content = self.facebookApi.get_url()
        instagram_response_content = self.instagramApi.get_personal_media()
        self.facebookParser.get_facebook_user_data(facebook_response_content)
        self.instagramParser.get_user_content(instagram_response_content)
        self.instagramParser.main()

        self.facebookExcel.save_to_excel(self.facebookParser.array_id)
        self.InstagramExcel.save_to_excel(self.instagramParser.array_likes)

def main():
    """
    Main method of the file
    :return:
    """

    analyzer = SocialMediaAnalyzer()
    analyzer.main()


if __name__ == '__main__':
    main()
