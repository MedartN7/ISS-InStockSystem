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
conn = None 
with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    def connect_to_database(): 
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id) as conn:
        

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
                conn.commit()

    def get_item_by_id(item_id):
        cur.execute(''' SELECT * FROM ITEMS WHERE Item_ID = %s; ''', (item_id,))
        return cur.fetchone()
    def get_item_by_name(name):
        cur.execute(''' SELECT * FROM ITEMS WHERE Name = %s; ''', (name,))
        return cur.fetchone()
    def get_item_by_price(price):
        cur.execute(''' SELECT * FROM ITEMS WHERE Price = %s; ''', (price,))
        return cur.fetchone()
    def get_item_by_brand(brand):
        cur.execute(''' SELECT * FROM ITEMS WHERE Brand = %s; ''', (brand,))
        return cur.fetchone()


    def update_item_id(item_id):
        cur.execute('''SELECT * FROM ITEMS WHERE Item_ID = %s;''', (item_id,))
        existing_item = cur.fetchone()
        if existing_item:
            return("ID number already occupied")
        else:
            cur.execute('''UPDATE ITEMS SET Item_ID = %s WHERE Item_ID = %s;''', (item_id, 1))
    def update_item_name(name):
        cur.execute('''UPDATE ITEMS SET Name = %s WHERE Item_ID = %s;''', (name))
        existing_item = cur.fetchone()
        if existing_item:
            return("Name already occupied")
        else:
            cur.execute('''UPDATE ITEMS SET Name = %s WHERE Item_ID = %s;''', (name, 1))
    def update_item_price(price):
        cur.execute('''UPDATE ITEMS SET Price = %s WHERE Item_ID = %s;''', (price))
        existing_item = cur.fetchone()
        if existing_item:
            return("That is current price")
        else:
            cur.execute('''UPDATE ITEMS SET Price = %s WHERE Item_ID = %s;''', (price, 1))
    def update_item_brand(brand):
        cur.execute('''UPDATE ITEMS SET Brand = %s WHERE Item_ID = %s;''', (brand))
        existing_item = cur.fetchone()
        if existing_item:
            return("Brand already exists")
        else:
            cur.execute('''UPDATE ITEMS SET Brand = %s WHERE Item_ID = %s;''', (brand, 1))


    def delete_item(item_id):
        cur.execute(''' DELETE FROM ITEMS WHERE Item_ID = %s; ''', (item_id))
        existing_item = cur.fetchone()
        if existing_item:
            return("Item does not exist")
        else:
            cur.execute(''' DELETE FROM ITEMS WHERE Item_ID = %s; ''', (item_id))

if cur is not None:
    cur.close()
if conn is not None:
    conn.close()
