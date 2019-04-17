class InstagramPosts:

    """
    Class to hold Data Attributes
    """

    def __init__(self, url=None, text=None, likes=None):
        self.url = url
        self.text = text
        self.likes = likes

        """
        Keep data from API and transfer to string 
        """

    def to_excel(self):
        return str(self.url), str(self.likes), str(self.text)
