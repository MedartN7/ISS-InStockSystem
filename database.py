import psycopg2
import psycopg2.extras
import json

with open('db_config.json', 'r') as config_file:
    config_data = json.load(config_file)

database_config = config_data.get('database_config', {})

hostname = database_config.get('hostname')
database = database_config.get('database')
username = database_config.get('username')
pwd = database_config.get('password')
port_id = database_config.get('port')
conn = None #usunąć?Może powodowac problem

#Utworzyć kopie tego pliku i zmodyfikowac nowy pod tą samą nazwą z funkcją łaczenia main.py
try:
    with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id) as conn:
    
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute(''' DROP TABLE IF EXISTS ITEMS;''')
            create_script = ''' CREATE TABLE IF NOT EXISTS ITEMS(
                Item_ID INT PRIMARY KEY,
                Name VARCHAR(100) NOT NULL,
                Price INT NOT NULL,
                Brand VARCHAR(100) NOT NULL); '''
            cur.execute(create_script)

            insert_script = ''' INSERT INTO ITEMS (Item_ID, Name, Price, Brand) VALUES (%s, %s, %s, %s); '''
            insert_default_data = [(1, 'Laptop', 1000, 'Dell'), 
                                (2, 'Mouse', 20, 'Logitech'), 
                                (3, 'Keyboard', 50, 'Logitech'),
                                (4, 'Monitor', 200, 'Ijama'),
                                (5, 'Headphones', 100, 'Sony')]
            for record in insert_default_data:
                cur.execute(insert_script, record)

            cur.execute(''' SELECT * FROM ITEMS; ''')
            for record in cur.fetchall():
                print(record['item_id'], record['name'], record['price'], record['brand'])

            update_name_script = ''' UPDATE ITEMS SET Name = %s WHERE Item_ID = %s; '''
            cur.execute(update_name_script, ('Laptop Pro', 1))

            delete_script = ''' DELETE FROM ITEMS WHERE Item_ID = %s; '''
            delete_record = (5,)
            cur.execute(delete_script, delete_record)

except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
