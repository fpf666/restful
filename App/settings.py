def get_database_uri(datainfo):
    dielict = datainfo.get('dielict') or 'mysql'
    drver = datainfo.get('driver') or 'pymysql'
    user = datainfo.get('user') or 'root'
    password = datainfo.get('password') or '1234'
    host = datainfo.get('host') or 'localhost'
    port = datainfo.get('port') or '3306'
    database = datainfo.get('database') or 'kog'
    #dielict+driver://user:password@host:port/database
    return '{}+{}://{}:{}@{}:{}/{}'.format(dielict,drver,user,password,host,port,database)

class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = '119'
    SESSION_TYPE = 'redis'
    SQLALCHEMY_DATABASE_URI = 'mysql+pysql://root:1234@localhost:3306/day05'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE = {
        'dielict':'mysql',
        'driver':'pymysql',
        'user':'root',
        'password':'12345678',
        'host':'localhost',
        'port':'3306',
        'database':'day05',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class TestConfig(Config):
    TESTING = True

    DATABASE = {
        'dielict': 'mysql',
        'drver': 'pymysql',
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'database': 'kog',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class ShowConfig(Config):
    DEBUG = True

    DATABASE = {
        'dielict': 'mysql',
        'drver': 'pymysql',
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'database': 'kog',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class OnlineConfig(Config):
    DEBUG = True

    DATABASE = {
        'dielict': 'mysql',
        'drver': 'pymysql',
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'database': 'kog',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

env = {
    'develop' : DevelopConfig,
    'test' : TestConfig,
    'show' : ShowConfig,
    'online' : OnlineConfig
}