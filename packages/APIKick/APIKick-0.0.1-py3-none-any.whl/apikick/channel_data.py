# apikick/channel_data.py
class ChannelData:
    def __init__(self, data: dict):
        # Initialize channel data attributes
        self.id: int = data.get("id")
        self.user_id: int = data.get("user_id")
        self.slug: str = data.get("slug")
        self.is_banned: bool = data.get("is_banned")
        self.playback: str = data.get("playback_url")
        self.vod_enabled: bool = data.get("vod_enabled")
        self.subscription_enabled: bool = data.get("subscription_enabled")
        self.followers_count: int = data.get("followers_count")
        self.subscriber_badges = [
            ChannelSubscriberBadges(badge)
            for badge in data.get("subscriber_badges", [])
        ]
        self.banner_image: str = data.get("banner_image")
        self.is_live: bool = bool(data.get("livestream"))

        if self.is_live:
            self.livestream_id: int = data.get("livestream", {}).get("id")
            self.slug: str = data.get("livestream", {}).get("slug")
            self.channel_id: int = data.get("livestream", {}).get("channel_id")
            self.created_at: str = data.get("livestream", {}).get("created_at")
            self.session_title: str = data.get("livestream", {}).get("session_title")
            self.is_live: bool = data.get("livestream", {}).get("is_live")
            self.risk_level_id = data.get("livestream", {}).get("risk_level_id")
            self.start_time: str = data.get("livestream", {}).get("start_time")
            self.source = data.get("livestream", {}).get("source")
            self.twitch_channel = data.get("livestream", {}).get("twitch_channel")
            self.duration: int = data.get("livestream", {}).get("duration")
            self.language: str = data.get("livestream", {}).get("language")
            self.is_mature: bool = data.get("livestream", {}).get("is_mature")
            self.viewer_count: int = data.get("livestream", {}).get("viewer_count")
            self.thumbnail_url: str = (
                data.get("livestream", {}).get("thumbnail", {}).get("url")
            )
            self.categories = [
                ChannelCategories(category)
                for category in data.get("livestream", {}).get("categories", [])
            ]

        self.role = data.get("role")
        self.muted: bool = data.get("muted")
        # TODO: Search the structure of the follower_badges
        # self.follower_badges: list = data.get("follower_badges", [])
        self.offline_banner_image: bool = data.get("offline_banner_image")

        if self.offline_banner_image:
            self.offline_banner_image_src: str = data.get("offline_banner_image").get(
                "src"
            )
            self.offline_banner_image_srcset: str = data.get(
                "offline_banner_image"
            ).get("srcset")

        self.verified: bool = data.get("verified")

        self.recent_categories = [
            ChannelCategories(category)
            for category in data.get("recent_categories", [])
        ]
        self.can_host: bool = data.get("can_host")
        self.username: str = data.get("user").get("username")
        self.agreed_to_terms: bool = data.get("user").get("agreed_to_terms")
        self.email_verified_at: str = data.get("user").get("email_verified_at")
        self.bio: str = data.get("user", {}).get("bio")
        self.country: str = data.get("user", {}).get("country")
        self.state: str = data.get("user", {}).get("state")
        self.city: str = data.get("user", {}).get("city")
        self.instagram: str = data.get("user", {}).get("instagram")
        self.twitter: str = data.get("user", {}).get("twitter")
        self.youtube: str = data.get("user", {}).get("youtube")
        self.discord: str = data.get("user", {}).get("discord")
        self.tiktok: str = data.get("user", {}).get("tiktok")
        self.facebook: str = data.get("user", {}).get("facebook")
        self.avatar: str = data.get("user", {}).get("profile_pic")
        self.chatroom: bool = bool(data.get("chatroom"))

        if self.chatroom:
            self.chatroom_id: int = data.get("chatroom").get("id")
            self.chatroom_chatable_type: str = data.get("chatroom").get("chatable_type")
            self.chatroom_channel_id: int = data.get("chatroom").get("channel_id")
            self.chatroom_created_at: str = data.get("chatroom").get("created_at")
            self.chatroom_updated_at: str = data.get("chatroom").get("updated_at")
            self.chatroom_mode_old: str = data.get("chatroom").get("mode_old")
            self.chatroom_chat_mode: str = data.get("chatroom").get("chat_mode")
            self.chatroom_slow_mode: bool = data.get("chatroom").get("slow_mode")
            self.chatroom_chatable_id: int = data.get("chatroom").get("chatable_id")
            self.chatroom_followers_mode: bool = data.get("chatroom").get(
                "followers_mode"
            )
            self.chatroom_subscribers_mode: bool = data.get("chatroom").get(
                "subscribers_mode"
            )
            self.chatroom_emotes_mode: bool = data.get("chatroom").get("emotes_mode")
            self.chatroom_message_interval: int = data.get("chatroom").get(
                "message_interval"
            )
            self.chatroom_following_min_duration: int = data.get("chatroom").get(
                "following_min_duration"
            )


class ChannelCategories:
    def __init__(self, data: dict):
        self.id: int = data.get("id")
        self.category_id: int = data.get("category_id")
        self.name: str = data.get("name")
        self.slug: str = data.get("slug")
        self.tags = [(tag) for tag in data.get("tags", [])]
        self.description: str = data.get("description")
        self.deleted_at = data.get("deleted_at")
        self.viewers: int = data.get("viewers")
        self.banner: bool = bool(data.get("banner"))

        if self.banner:
            self.banner_responsive: str = data.get("banner").get("responsive")
            self.banner_url: str = data.get("banner").get("url")

        self.category = ChannelCategory(data.get("category"))


class ChannelCategory:
    def __init__(self, data: dict):
        self.id: int = data.get("id")
        self.name: str = data.get("name")
        self.slug: str = data.get("slug")
        self.icon: str = data.get("icon")


class ChannelSubscriberBadges:
    def __init__(self, data: dict):
        self.id: int = data.get("id")
        self.channel_id: int = data.get("channel_id")
        self.months: int = data.get("months")
        self.badge_image_srcset: str = data.get("badge_image").get("srcset")
        self.badge_image_url: str = data.get("badge_image").get("src")
