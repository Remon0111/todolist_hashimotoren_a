from flask import Flask, render_template, jsonify, request
from flask_login import UserMixin, login_manager, login_user, logout_user
import sqlite3


app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('WebTodo.html')

@app.route("/process", methods=["POST"])
def post_list():
    conn = sqlite3.connect('taskSql.db')
    cursor = conn.cursor()
    todoName = request.form['todoName']
    todoYear = request.form['todoYear']
    todoMonth = request.form['todoMonth']
    todoDay = request.form['todoDay']
    todoHour = request.form['todoHour']
    cursor.execute('INSERT INTO todolist(taskName, taskYear, taskMonth, taskDay, taskHour, checkMark) values(?, ?, ?, ?, ?, ?)', (todoName, todoYear, todoMonth, todoDay, todoHour, "×"))
    conn.commit()
    conn.close()
    return jsonify(status=200)

@app.route('/send-list', methods=['GET'])
def send_list():
    # 送信するリスト
    conn = sqlite3.connect('taskSql.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todolist")
    data = cursor.fetchall()
    result_list = data
    conn.close()
    # リストをJSON形式で返す
    return jsonify({"list": result_list})

@app.route("/update_todo", methods=["POST"])
def update_list():
    conn = sqlite3.connect('taskSql.db')
    cursor = conn.cursor()
    updateTaskNumber = request.form['updateTaskNumber']
    idNumber = int(updateTaskNumber)
    updateTaskContent = request.form['updateTaskContent']
    updateTaskInput = request.form['updateTaskInput']
    cursor.execute(f'UPDATE todoList SET {updateTaskContent} = "{updateTaskInput}" WHERE id = {idNumber}')
    conn.commit()
    conn.close()
    return jsonify(status=200)

@app.route("/reporting_todo", methods=["POST"])
def reporting_list():
    conn = sqlite3.connect('taskSql.db')
    cursor = conn.cursor()
    reportingNumber = request.form['reportingNumber']
    idNumber = int(reportingNumber)
    reportingMark = request.form['reportingMark']
    cursor.execute(f'UPDATE todoList SET checkMark = "{reportingMark}" WHERE id = {idNumber}')
    conn.commit()
    conn.close()
    return jsonify(status=200)

@app.route("/delete_todo", methods=["POST"])
def delete_list():
    conn = sqlite3.connect('taskSql.db')
    cursor = conn.cursor()
    deleteNumber = request.form['deleteNumber']
    idNumber = int(deleteNumber)
    cursor.execute(f'DELETE FROM todoList WHERE id = {idNumber}')
    conn.commit()
    conn.close()
    return jsonify(status=200)

if __name__ == '__main__':
    app.debug = True
    app.run()