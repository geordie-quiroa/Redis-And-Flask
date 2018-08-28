import redis
from flask import Flask, render_template, request
app = Flask(__name__)
conn = redis.StrictRedis(host='209.97.137.35', port='281')

@app.route('/', methods = ['GET', 'POST'])
def homepage():
	try:
		llaves = conn.keys()
		texto = "Llaves disponibles en el container de redis:"
		placeholder_buscar = "Valor a buscar en Redis DB  (Presionar ENTER)"
		return render_template('index.html', texto = texto, placeholder_buscar = placeholder_buscar, llaves = llaves )
	except Exception as e:
		return str(e)
@app.route('/busqueda', methods = ['GET', 'POST'])
def buscar():
	try:
		buscar_valor = request.form['buscar_valor']
		valor = conn.get(buscar_valor)
		if valor is None:
			valor = "El valor consultado no existe."
		return render_template("resultados.html", buscar_valor = buscar_valor, valor = valor)
	except Exception as e:
		return str(e)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
