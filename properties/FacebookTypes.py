from configurations import *
import facebook



class FacebookTypes():
    def __init__(self):
        pass

    def request_to_facebook(self):
        token = 'EAAE3g14kRzEBABUH3j7O057YdZCLfpa2WcA0WJGnnX5ZCfyTkcSEM0UCGHtdxMSnYP35TW4MEGuoLUVaIblR0qNZC4HYb8IlvZB5getd95ZAjuAh3oXvZAQhZBbVgIGUccsivQzb8ZBUGR5pypG9RDjwk3AHv5hhjDcZD'
        graph = facebook.GraphAPI(access_token=token, version="2.12")
        posts = graph.request('2125055407548376/posts')
        return posts
