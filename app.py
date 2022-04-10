from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'ali'
app.config['MYSQL_PASSWORD'] = 'Testing@1234'
app.config['MYSQL_DB'] = 'movies'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM movies")
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', movies=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        flash("Data Inserted Successfully")
        type = request.form['type']
        name = request.form['name']
        total_ep = request.form['total_ep']
        actual_ep = request.form['actual_ep']
        last_view = request.form['last_view']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO movies (type, name, total_ep, actual_ep, last_view) VALUES %d, %s, %d, %d, %s",
            (type, name, total_ep, actual_ep, last_view),
        )
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM movies WHERE id=%d", (id,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        type = request.form['type']
        name = request.form['name']
        total_ep = request.form['total_ep']
        actual_ep = request.form['actual_ep']
        last_view = request.form['last_view']
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE movies SET type=%d, name=%s, total_ep=%d, actual_ep=%d, last_view=%s) WHERE id=%d",
            (type, name, total_ep, actual_ep, last_view),
        )
        flash("DATA Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))
