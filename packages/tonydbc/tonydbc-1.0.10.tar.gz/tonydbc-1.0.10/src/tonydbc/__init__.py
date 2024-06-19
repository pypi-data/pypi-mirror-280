"""
tonydbc

    TonyDBC: A context manager for mariadb data connections.

    MQTTClient: A context manager for an MQTT client

    create_test_database: function to create a complete test database

Note: you should define the following environment variables before using this library, e.g.

    CHECK_ENVIRONMENT_INTEGRITY = True
    DOT_ENVS                    = ["..\\..\\.env", ".env"]
    USE_PRODUCTION_DATABASE     = True
    PRODUCTION_DATABASES        = ["master_db", "master2_db", "etc"]
    MYSQL_TEST_DATABASE         = test_db
    MYSQL_PRODUCTION_DATABASE   = master_db
    # Full list is at pytz.all_timezones
    DEFAULT_TIMEZONE            = Asia/Singapore  
    DEFAULT_TIME_OFFSET         = +08:00
    MEDIA_BASE_PATH_PRODUCTION  = C:\\

e.g. 
    import tonydbc
    tonydbc.load_dotenvs()

"""
__version__ = "1.0.10"

from .env_utils import get_env_bool, get_env_list, load_dotenv, load_dotenvs
from .tony_utils import (
    set_MYSQL_DATABASE,
    get_current_time,
    get_current_time_string,
    deserialize_table,
)
from .tonydbc import TonyDBC
from .mqtt_client import MQTTClient
from .dataframe_fast import DataFrameFast
from .create_test_database import create_test_database
