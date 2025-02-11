from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal que renderiza la plantilla HTML
@app.route("/")
def index():
    titulo = "IDGS801"
    lista = ["pedro", "Juan", "Yael"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")


@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")



# Ruta simple que muestra un mensaje en HTML
@app.route("/hola")
def hola():
    return "<h1>Hello world ----Nuevo---</h1>"

# Ruta que recibe un string como parámetro
@app.route("/use/<string:user>")
def user(user):
    return f"<h1>Hola, {user}</h1>"

# Ruta que recibe un número entero
@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El número es: {n}</h1>"

# Ruta que recibe un ID y un nombre de usuario
@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>El usuario {username} tiene el ID {id}</h1>"

# Ruta que recibe dos números flotantes y devuelve la suma
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma de {n1} + {n2} es {n1 + n2}</h1>"

# Ruta con parámetro opcional (se corrigió un error en el código)
@app.route("/default/")
@app.route("/default/<string:param>")
def default(param="Sin valor"):
    return f"<h1>El parámetro recibido es: {param}</h1>"

# Ruta que devuelve un formulario HTML
@app.route("/operas/")
def operas():
    return '''
    <form>
        <label for="num1">Número 1:</label>
        <input type="text" id="num1" name="num1">
        <label for="num2">Número 2:</label>
        <input type="text" id="num2" name="num2">
        <button type="submit">Enviar</button>
    </form>
    '''

# Ejecutar la aplicación en modo debug en el puerto 3000
if __name__ == "__main__":
    app.run(debug=True, port=3000)


