from PURVIMUSIC.core.bot import PURVI
from DISHA_QWEEN.core.dir import dirr
from DISHA_QWEEN.core.git import git
from DISHA_QWEEN.core.userbot import Userbot
from DISHA_QWEEN.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DISHA()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
