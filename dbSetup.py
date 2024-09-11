import sqlite3

dbname = 'taskSql.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
cur.execute('CREATE TABLE todoList(id INTEGER PRIMARY KEY AUTOINCREMENT, taskName STRING, taskYear, taskMonth, taskDay, taskHour, checkMark)')

# データベースへコミット。これで変更が反映される。
conn.commit()