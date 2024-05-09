#11.1
import zoo
zoo.hours()
#11.2
import zoo as menagerie
menagerie.hours()
#16.8
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
    print(row)
