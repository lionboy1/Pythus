import sqlite3

def connect():
    conn = sqlite3.connect("contacts.db") #create the database
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contact_table(id INTEGER PRIMARY KEY, Client text, Email text, Phone integer, Address text)")#create the table to store data
    conn.commit()# execute the database
    conn.close()

def insert(Client, Email, Phone, Address):
    conn= sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contact_table VALUES (NULL,?,?,?,?)",(Client, Email, Phone, Address))
    conn.commit()
    conn.close()

def view():
    conn= sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact_table")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(Client="", Email="", Phone="", Address=""):
    conn= sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact_table WHERE Client=? OR Email=? OR Phone=? OR Address=?", (Client, Email, Phone, Address) )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):# id tuple from data displayed in listbox.
    conn= sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contact_table WHERE id=?", (id,) )#first id is column name and second is parameter argument passed back into function
    conn.commit()
    conn.close()

def update(id, Client, Email, Phone, Address):
    conn= sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("UPDATE contact_table SET Client=?, Email=?, Phone=?, Address=? WHERE id=?", (Client, Email, Phone, Address, id) )#Update table changes by the SET. Do not try to update id values.
    conn.commit()
    conn.close()

connect()# function must be called to run database setup above.
