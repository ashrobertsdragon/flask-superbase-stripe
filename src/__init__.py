from decouple import config
from flask import Flask

# Config classes for environment variables
from config import DevelopmentConfig, TestingConfig, StagingConfig, ProductionConfig

app = Flask(__name__)

env_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}

# Load environment variable for flask environment configuration class
config_name = config("FLASK_ENV", default="development")
app.config.from_object(env_config[config_name])
