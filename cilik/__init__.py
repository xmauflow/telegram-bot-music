from cilik.core.bot import CilikBot
from cilik.core.dir import dirr
from cilik.core.userbot import Userbot
from cilik.misc import dbb, heroku, sudo

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
cilik = CilikBot()

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
