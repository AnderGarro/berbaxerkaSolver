from flask import Flask, render_template, request, url_for, flash, redirect
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route('/', methods=('GET', 'POST'))
def create():
    list = [""]
    if request.method == 'POST':
        letters = request.form['letters']
        pivot = request.form['pivot']
        print(letters,pivot)
        if pivot not in letters:
            letters = letters + pivot
        if not letters or not pivot:
            flash('Sartu letrak!')
        elif len(pivot) != 1:
            flash('Sartu letra bat letra komun blokean!')
        elif len(letters) > 10:
            flash('10 letra maximo!')
        else:
            list = get_words_from_letters(letters, pivot)
    return render_template('create.html', words = list)

def get_db_connection():
    config = {
      'user': 'berbauser',
      'password': 'berbapass54321',
      'host': 'db',
      'database': 'db',
      'raise_on_warnings': True
    }
    cnx = mysql.connector.connect(**config)
    return cnx

def close_db_connection(cnx):
    cnx.close()

def get_words_from_letters(letters, pivot):
    conn = get_db_connection()
    query = """SELECT lema FROM hitzak WHERE lema RLIKE '^(["""+list_to_string(letters)+"""+])+$' AND lema LIKE "%"""+pivot+"""%";"""
    print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    list = []
    for item in cursor:
        list.append(item[0])
    close_db_connection(conn)
    return list

def list_to_string(list):
    str=""
    for item in list:
        str = str + item + ","
    if len(str) > 0:
        str = str[:-1]
    return str

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
