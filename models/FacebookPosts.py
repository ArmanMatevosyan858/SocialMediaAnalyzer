class FacebookPosts:
    def __init__(self, message=None, id=None, time=None):
        self.message = message
        self.id = id
        self.time = time

    def to_excel(self):
        return str(self.message), str(self.id), str(self.time)
