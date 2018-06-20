import json
import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = 'r@thn@m4'
DATABASE = 'movieinfo'

db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE)
cursor = db.cursor()

imdb_list = open('imdb.json', 'r').read()
data = json.loads(imdb_list)
for rec in data:
    print(rec)

    query = "INSERT INTO movinfo_movies (popularity, director, genre, imdb_score, name) values('%d', '%s', '%s', '%2f', '%s')"
    popularity, director, genre, imdb_score, name = rec['99popularity'],\
                rec['director'], rec['genre'], rec['imdb_score'], rec['name']
    strip_list = [item.strip() for item in genre]
    values = (popularity, director, '<>'.join(strip_list), imdb_score, name)
    cursor.execute(query%values)
    db.commit()
