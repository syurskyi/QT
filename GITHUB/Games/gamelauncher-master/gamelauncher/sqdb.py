import sqlite3
connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()

#cursor.execute('insert into student values(?, ?)', (1, 'Anim'))
#cursor.execute('insert into student values(?, ?)', (2, 'Helly'))
cursor.execute('insert into s1 values(?, ?)', (3, 'Anis'))
#cursor.execute('create table if not exists s1(id integer primary key, name text)')
connection.commit()

#cursor.execute('select * from student')
#row = cursor.fetchall()
#for r in row:
#    print(r)


