from models.BaseClass import BaseClass
from network.Instagram import Instagram
from parsers.InstagramParser import InstagramParser
from output.InstagramExcel import InstagramExcel

class SocialMediaAnalyzer(BaseClass):
    """
    Main class
    """

    def __init__(self):
        """
        Initialization of the class
        """

        self.instagramApi = Instagram()
        self.InstagramExcel = InstagramExcel()
        self.instagramParser = InstagramParser()


    def main(self):
        """
        Main method of the class
        :return:
        """

        instagram_response_content = self.instagramApi.get_personal_media()
        self.debug(instagram_response_content)
        self.instagramParser.get_user_content(instagram_response_content)
        self.instagramParser.main()
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
