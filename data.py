import sqlite3

db = sqlite3.connect('app.db')
cr = db.cursor()
cr.execute('CREATE TABLE IF NOT EXISTS employee(id TEXT, name TEXT, age INTEGER, gender TEXT, role TEXT)')

def id():
    cr.execute('SELECT id FROM employee')
    try:
        last_id = cr.fetchall()[-1]
        counter = int(last_id[0]) + 1
    except:
        counter = 1
    return counter

def insert_employees(id, name, age, gender, role):
    cr.execute(f'INSERT INTO EMPLOYEE (id, name, age, gender, role) VALUES("{id}", "{name}", {age}, "{gender}", "{role}")')
    db.commit()

def get_data():
    cr.execute('SELECT * FROM employee')
    data = cr.fetchall()
    return data

def delete_from_db(id):
    cr.execute(f'delete from employee where id  = {id}')
    db.commit()

def get_row(id):
    data = get_data()
    for i in data:
        if id == int(i[0]):
            return i
        else:
            pass

def clr_data():
    cr.execute('DELETE FROM employee')
    db.commit()