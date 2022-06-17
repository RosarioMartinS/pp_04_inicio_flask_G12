from flask import Flask
import datetime
import random
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'



@app.route('/dado')
def numeroAleatorio():
    numRandom=random.randrange(1, 7)
    return f"<h1>El numero es {numRandom}</h1>"

@app.route('/fecha')
def devuelveFecha():
    fecha1 = datetime.date(1970, 1, 1)
    fecha2 = datetime.date(2100, 12, 31)
    diferenciaFechas= (fecha2- fecha1).days
    cantDiasAleatorio=random.randrange(diferenciaFechas)
    numRandom = fecha1 +datetime.timedelta(days=cantDiasAleatorio)
    return f"<h1> La fecha es  {numRandom}</h1>"
  
@app.route('/color')
def devuelveColor():
    r=random.randint(0,256)
    b=random.randint(0,256)
    g=random.randint(0,256)
    rgb=f"rgb({r}, {b}, {g})"
    return f'<h1 style="color:{rgb}">El color elegido fue {r}, {b}, {g}</h1>'

@app.route('/dado/<n>')
def devuelveNNumeros(n):
    i=0
    n=int(n)
    numeros=""
    if n >=0 or n<10: 
      for i in range(n):
        numeros += f"{str(random.randrange(1, 7))}\n"
    else:
        return f"ERROR El número es mayor que 10 o menor que 0. Por favor intente nuevamente con otro"
    return f"<h1>Estos son los valores aleatorios obtenidos:\n {numeros}</h1>"

@app.route('/fecha/<y>')
def delvuelveFechaConAñoY(y):
    y=int(y)
    fecha1 = datetime.date(y, 1, 1)
    fecha2 = datetime.date(y, 12, 31)
    diferenciaFechas= (fecha2- fecha1).days
    cantDiasAleatorio=random.randrange(diferenciaFechas)
    numRandom = fecha1 +datetime.timedelta(days=cantDiasAleatorio)
    return f"<h1> La fecha es  {numRandom}</h1>"
@app.route('/fecha/<y>/<m>')
def devuelveFechaConAñoYYMesM(y,m):
    y=int(y)
    m=int(m)
    if m<12:
      fecha1 = datetime.date(y, m, 1)
      fecha2 = datetime.date(y, m, 31)
      diferenciaFechas= (fecha2- fecha1).days
      cantDiasAleatorio=random.randrange(diferenciaFechas)
      numRandom = fecha1 +datetime.timedelta(days=cantDiasAleatorio)
    else:
      return "El mes debe ser menor a 12 "
    return f"<h1> La fecha es  {numRandom}</h1>"
  
app.run(host='0.0.0.0', port=81)

