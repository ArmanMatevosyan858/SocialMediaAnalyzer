import json
from models.FacebookPosts import FacebookPosts
import ast

class FacebookParser:
    def __init__(self):
        self.array_id = []

    def get_facebook_user_data(self, facebook_response_content):
        for data in facebook_response_content['data']:
            print(data)
            message = None
            id = None
            time = None
            if 'id' in data:
                id = data['id']
            if 'message' in data:
                message = data['message']
            if 'created_time' in data:
                time = data['created_time']
            self.array_id.append(FacebookPosts(message=message, id=id, time=time))
