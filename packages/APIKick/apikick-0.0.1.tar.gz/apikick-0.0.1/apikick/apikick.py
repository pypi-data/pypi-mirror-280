# apikick/kickapi.py
import time
import requests
from .utils.validate import validate_username, validate_video_id
from .channel_data import ChannelData
from .video_data import VideoData
from .chat_data import ChatData


class KickAPI:
    def __init__(self):
        # Initialize the session and set headers and cookies
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json",
            "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
            "Alt-Used": "kick.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        }

    def channel(self, username: str):
        # Get channel data by username
        validate_username(username)
        url = f"https://kick.com/api/v1/channels/{username}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return ChannelData(data)
        except:
            if response.status_code == 403:
                print("Trying to get channel data again...")
                time.sleep(3)
                return self.channel(username)

            print("Failed to parse JSON response.")
            return None

    def video(self, video_id: str):
        # Validate video ID
        validate_video_id(video_id)
        # Get video data by video ID
        url = f"https://kick.com/api/v1/video/{video_id}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return VideoData(data)
        except ValueError:
            if response.status_code == 403:
                print("Trying to get video data again...")
                time.sleep(3)
                return self.video(video_id)
            print("Failed to parse JSON response.")
            return None

    def chat(self, channel_id: str, datetime: str):
        # Get chat data by channel id
        url = f"https://kick.com/api/v2/channels/{channel_id}/messages?start_time={datetime}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return ChatData(data)
        except ValueError:
            print("Failed to parse JSON response.")
            return None
