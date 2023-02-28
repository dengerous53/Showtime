import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = "Media_search"
API_ID = int(13985209)
API_HASH = "9ecc14b98a6c7bfbc445f3b425a56e21"
BOT_TOKEN = "5375286492:AAGDTnq9zh1vBDzNkwMTddW-sQLAU7ensxw"
# Bot settings
CACHE_TIME = int(300)
USE_CAPTION_FILTER = False 
PICS = ["https://graph.org/file/8772d71746e2fdca86ae2.jpg", "https://graph.org/file/96b93bc4465d3e245baf5.jpg"]

# Admins, Channels & Users
ADMINS = [1314385986, 5797297120]
CHANNELS = None
AUTH_USERS = ADMINS
AUTH_CHANNEL = int(-1001652975277)
AUTH_GROUPS = None

# MongoDB information
DATABASE_URI = "mongodb+srv://nitish:nitish876@cluster0.3dspllq.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "noseen"
COLLECTION_NAME = "Telegram_files"

# Others
LOG_CHANNEL = int(-1001769350923)
SUPPORT_CHAT = "showtimemovierequest"
P_TTI_SHOW_OFF = is_enabled(("False"), False)
IMDB = is_enabled(("False"), False)
SINGLE_BUTTON = is_enabled(("True"), True)
CUSTOM_FILE_CAPTION = None
BATCH_FILE_CAPTION = None
IMDB_TEMPLATE = "🎬 𝙵ɪʟᴍ : <a href={url}>{title}</a>\n🧩 𝚈ᴇᴀʀ : <a href={url}/releaseinfo>{year}</a>\n☠ 𝚁ᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a>\n🔊 𝙻ᴀɴɢᴜᴀɢᴇ : {languages}\n\n🦋 Requested by : {message.from_user.mention}\n🎯 Uploaded by: {message.chat.title}"
LONG_IMDB_DESCRIPTION = False 
SPELL_CHECK_REPLY = is_enabled(("True"), True)
MAX_LIST_ELM = None
INDEX_REQ_CHANNEL = LOG_CHANNEL
FILE_STORE_CHANNEL = None
MELCOW_NEW_USERS = is_enabled(("True"), True)
PROTECT_CONTENT = is_enabled(("False"), False)
PUBLIC_FILE_STORE = is_enabled(("True"), True)
WEB_LINK = "https://tnlink.in/api"
API_KEY = "b9558942eb7ba391657e1542a8e050340090bdd5"

# Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "False":
    SELF_DELETE = False
