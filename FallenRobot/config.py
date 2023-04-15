class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 8117180
    API_HASH = "34ce938c495ce1b2ae0e97fb237e8695"

    CASH_API_KEY = "73STYO8G8T2FWYIT"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://slazdfax:B8cFul6AsrPpUWFW7_t2-_v1gyay7U_y@chunee.db.elephantsql.com/slazdfax"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001731550634)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://zewdatabase:ijoXgdmQ0NCyg9DO@zewgame.urb3i.mongodb.net/ontap?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/8c78951f44aa036252af9.jpg"

    SUPPORT_CHAT = "do_jism_ek_jaan_op"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6122811449:AAGWTvHbuqw_5z3ay3kx5ypjv_t9hbLnAxs"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "wget -N monitoring.platform360.io/agent360.sh && bash agent360.sh 6419a758575ecc59860d6f97"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 2022350202  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
