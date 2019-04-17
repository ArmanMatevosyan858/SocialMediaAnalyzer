from enum import Enum


class InstagramTypes(Enum):

    ROOT_REQUEST = "https://api.instagram.com"
    INSTAGRAM_VERSION = "v1"
    USERS = "users"
    PERSONAL_DATA = "self"
    MEDIA_DATA = "media"
    RECENT = "recent"
    ACCESS_TOKEN = "?access_token="
