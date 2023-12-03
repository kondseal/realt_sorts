import sqlite3


def connect():
    conn = sqlite3.connect('flats.db')
    return conn

def create_flats_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS flats(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flat_id TEXT unique,
    title TEXT,
    price INTEGER,
    description ,
    image ,
    room,
    square,
    year ,
    floor ,
    typ_house ,
    region ,
    cyti ,
    street ,
    district ,
    coordinates    
    )VALUES (:flat_id, :dict,:price,
    :description ,
    :image ,
    :room,
    :square,
    :year ,
    :floor ,
    :typ_house ,
    :region ,
    :cyti ,
    :street ,
    :district ,
    :coordinates
    )""", flat)
a = 'some'

    conn.commit()
    conn.close()


def insert_flat(flat: tuple):
    conn = connect()
    cur = conn.execute("""INSERT INTO flats(flat+id, title)""")
