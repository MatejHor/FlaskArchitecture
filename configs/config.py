import os


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = "secret_key"
    SQLALCHEMY_DATABASE_URI = (
            "postgresql://"
            + (os.getenv("POSTGRES_USER") or 'postgres')
            + ":"
            + (os.getenv("POSTGRES_PASSWORD") or 'postgres')
            + "@"
            + (os.getenv("POSTGRES_HOST") or 'localhost')
            + "/"
            + (os.getenv("POSTGRES_DB") or 5432)
    )
    os.environ["DATABASE_URL"] = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    DEBUG = True
