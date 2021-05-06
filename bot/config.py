from os.path import abspath, dirname, join


BASEDIR = abspath(dirname(__file__))

BOT_SETUP = {
    "token": "1721306485:AAHmkuQAtcM_9APBEyj4N35fFhhZBRe9ZT8",
    "threaded": False,
    "skip_pending": True,
    "parse_mode": "HTML"
}


class Config:

    # Folders and files
    root_folder = BASEDIR
    project_folder = join(BASEDIR, "project")

    # Admin
    admins = []

    secret = 'rqyrfwaioueoughpaeouigh'
    webhook_url = 'https://hachathonbot.savvamirzoyan.xyz/' + secret


class AppConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(BASEDIR, "main.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "svbjdjsbzdpodvbp83uqrv"