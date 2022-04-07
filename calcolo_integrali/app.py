from lib2to3.pygram import Symbols
from flask import Flask, render_template, request, make_response, redirect, url_for
import sqlite3
from datetime import datetime
import sympy

#Inizializzazione Sympy
x,y,z = sympy.symbols('x y z')
sympy.init_printing(use_unicode=True)

#Flask
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

#Login
def index():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if validate(username, password):
      resp = make_response(redirect(url_for('integrali')))
      resp.set_cookie('username', username)
      print(request.cookies.get('username'))
      return resp
  return render_template('login.html')
  

def validate(username, password):
    con = sqlite3.connect('flask_examples/Es1/db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    for row in rows:
        if row[0]==username and row[1] == password:
            return True
    
    return False


#Integrali
@app.route(f'/integrali', methods=['GET', 'POST'])
def integrali():
  con = sqlite3.connect('flask_examples/Es1/integrali.db')
  cur = con.cursor()

  if request.method == 'POST':
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    i = request.form['integrale']
    e1 = request.form['estremo1']
    e2 = request.form['estremo2']

    print(e1)
    print(e2)

    if e1 == '' or e2 == '':
      print(f"{request.cookies.get('username')}: {sympy.integrate(i, x)}")
      cur.execute(f"INSERT INTO integrali (utente, data, integrale, risultato) VALUES ('{request.cookies.get('username')}','{dt_string}','{i}','{sympy.integrate(i, x)}')")
    else:
      print(f"{request.cookies.get('username')}: {sympy.integrate(i, (x,e1,e2))}")
      cur.execute(f"INSERT INTO integrali (utente, data, integrale, risultato) VALUES ('{request.cookies.get('username')}','{dt_string}','{i}','{sympy.integrate(i, (x,e1,e2))}')")
  
  con.commit()
  return render_template("integrali.html")


app.run(debug=True, host='localhost')