
import os

que = {}
admins = {}

BG_IMG = os.environ.get("BG_IMG", "https://i.imgur.com/W3Jyec6.jpg")
START_PIC = BG_IMG
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "DragonEyeGaming")

SESSION_STRING = os.environ.get("SESSION_STRING", "BQBiMZkAwteEVUvkjjCfMVQezEPtjcKuzAraomRjutEbJeQ29N-LY4DlCrdwqXsRHG36bwk0fsSTzst0JIF8F0HFSMbkrR_qJdjRPP5QzDb5bQefhyZjjm4wgoFsOhxPLKM46VdhGSk89E2S2moCrPUaMUV_yzBZQKh9ic8B69jqD_9YAFwk45AZXEpwh8JYgcGlKJ6qZAR0cJBEwkYdVzt4N8CVu2325fTFs4yQ_I05dEbQvz0KWEKdeqGHaGQaFVOWbk1A_5T0N0RaA0TsMtD1JPAmEGav1WOxO79Ldo7YQHnRnHDn2FaC_o64mTg_KyuNh9QKp_Qz3NHjNrZ7I6EJbi4VtAAAAAFjLzPOAA")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5794025656:AAGS23V5-OBBklOdktS88DUEAHuOZsZ144Q")
API_ID = int(os.environ.get("API_ID", "21886785"))
API_HASH = os.environ.get("API_HASH", "6eec5fe78d63996edcc564ffb00a7e9f")
OWNER_ID = int(os.environ.get("OWNER_ID", "1936119750"))
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","Devs_discussion" )
UPDATE = os.environ.get("UPDATE", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05d76dc3-6e63-462c-a0f1-f5253e663369")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "kurumiopmusic")
DURATION_LIMIT = int(os.environ.get("DURATION_LIMIT", "600"))
CMD_MUSIC = list(os.environ.get("CMD_MUSIC", "/ !").split())
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb://mongo:cdxXUD3JvqaAQUH7NuL7@containers-us-west-114.railway.app:5690")
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", -1001809288523)


SUDO_USERS = (OWNER_ID, 5698598401)
