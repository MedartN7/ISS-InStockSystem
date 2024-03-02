import psycopg2
import json

with open('db_config.json', 'r') as config_file:
    config_data = json.load(config_file)

database_config = config_data.get('database_config', {})

hostname = database_config.get('hostname')
database = database_config.get('database')
username = database_config.get('username')
pwd = database_config.get('password')
port_id = database_config.get('port')

conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id
    )

