
class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://roma:5252@localhost/races'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'