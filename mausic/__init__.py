from mausic.core.bot import MausicBot
from mausic.core.dir import dirr
from mausic.core.userbot import Userbot
from mausic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()


# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
mausic = MausicBot()

# Assistant Client
ub = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
