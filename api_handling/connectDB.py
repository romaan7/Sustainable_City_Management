import psycopg2, os
import configparser

config = configparser.ConfigParser()
CFG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
config.read(CFG_DIR)

conn = psycopg2.connect(database=config.get('AWS', 'database'), user=config.get('USERS_CREDS', 'user'), password=config.get('USERS_CREDS', 'pwd'), host=config.get('AWS', 'host'))
