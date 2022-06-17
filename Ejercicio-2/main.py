from flask import Flask, render_template
import sqlite3

app = Flask(__name__,template_folder='templates')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ayuda')
def ayuda():
  return render_template("ayuda.html")

@app.route('/listado')
def mostrarListadoCapita():
  conn = sqlite3.connect('co_emissions.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("""SELECT *
                        FROM emissions
                        WHERE Series = "pcap"
                        ORDER BY Value DESC
                        LIMIT 10;
                    """)
  rows = cur.fetchall()
  return render_template("listadoPerCapita.html", rows=rows)

@app.route('/listado/top')
def mostrarListadoTotal():
  conn = sqlite3.connect('co_emissions.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("""SELECT *
                        FROM emissions
                        WHERE Series = "total"
                        ORDER BY Value DESC
                        LIMIT 10;
                    """)
  rows = cur.fetchall()
  return render_template("listadoTotal.html", rows=rows)



@app.route('/listado/<pais>')
def mostrarListadoPais(pais):
  conn = sqlite3.connect('co_emissions.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute(f"""SELECT *
                        FROM emissions
                        WHERE Country LIKE '{pais}'
                        ORDER BY Value DESC;
                    """)
  rows = cur.fetchall()
  return render_template("listadoSegunPais.html", rows=rows,pais=pais )
@app.route('/paises')
def mostrarPaises():
  conn = sqlite3.connect('co_emissions.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute(f"""SELECT DISTINCT Country
                        FROM emissions
                        
                    """)
  rows = cur.fetchall()
  return render_template("paises.html", rows=rows)
app.run(host='0.0.0.0', port=81)