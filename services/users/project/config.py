#services/users/project/config.py

class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """"Development cofiguration"""
    pass    

class TestingConfig(BaseConfig):
    """"Testing cofiguration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """"Production cofiguration"""
    pass