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
BOT_TOKEN = "5375286492:AAENZ0XB18lh8RdFlh2CBNem5BQ0ucwLLfU"
# Bot settings
CACHE_TIME = int(300)
USE_CAPTION_FILTER = False 
PICS = "https://te.legra.ph/file/d4b4d903dcdf2be77871b.jpg"

# Admins, Channels & Users
ADMINS = [1314385986, 5797297120]
CHANNELS = None
auth_users = None
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = [-1001877635960]
auth_grp = None
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None


# MongoDB information
DATABASE_URI = "mongodb+srv://nitish:nitish876@cluster0.3dspllq.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "noseen"
COLLECTION_NAME = "Telegram_files"

# Others
LOG_CHANNEL = int(-1001769350923)
SUPPORT_CHAT = "showtimemovierequest"
P_TTI_SHOW_OFF = is_enabled(("False"), False)
IMDB = is_enabled(("True"), True)
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

