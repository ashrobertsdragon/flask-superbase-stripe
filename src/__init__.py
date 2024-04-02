from decouple import config
from flask import Flask

# Config classes for environment variables
from config import DevelopmentConfig, TestingConfig, StagingConfig, ProductionConfig

# Import blueprints
from accounts.views import accounts_bp
from core.views import core_bp
from paid.views import paid_bp

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
app.register_blueprint(paid_bp)

env_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}

# Load environment variable for flask environment configuration class
config_name = config("FLASK_ENV", default="development")
app.config.from_object(env_config[config_name])
