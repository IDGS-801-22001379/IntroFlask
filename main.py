from flask import Flask, render_template, request, flash, jsonify
from flask import Flask, render_template, request

# Crear la aplicación Flask
app = Flask(__name__)
app.secret_key = "clave_secreta"

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


@app.route('/OperasBas', methods=["GET", "POST"])
def operas1():
    resultado = None
    mensaje = None

    if request.method == "POST":
        try:
            n1 = float(request.form.get("n1", "0"))
            n2 = float(request.form.get("n2", "0"))
            operacion = request.form.get("operacion")

            if operacion == "suma":
                resultado = n1 + n2
            elif operacion == "resta":
                resultado = n1 - n2
            elif operacion == "multiplicacion":
                resultado = n1 * n2
            elif operacion == "division":
                if n2 == 0:
                    mensaje = "No se puede dividir entre 0"
                else:
                    resultado = n1 / n2
        except ValueError:
            mensaje = "Por favor, ingresa números válidos."

    return render_template("OperasBas.html", resultado=resultado, mensaje=mensaje)



'''-------------------------------------------------cinepolis-------------------------------------------------------------------------------'''


@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    total_pagar = None
    resumen_compra = None

    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            cantidad_compradores = int(request.form["cantidad_compradores"])
            cantidad_boletos = int(request.form["cantidad_boletos"])
            usa_cineco = request.form["tarjeta"] == "si"

            precio_boleta = 12
            total = precio_boleta * cantidad_boletos
            descuento = 0

            max_boletos = cantidad_compradores * 7
            if cantidad_boletos > max_boletos:
                flash(f"No puedes comprar más de {max_boletos} boletos.", "danger")
            else:
                if cantidad_boletos > 5:
                    descuento = total * 0.15
                elif 3 <= cantidad_boletos <= 5:
                    descuento = total * 0.10
                
                total -= descuento

                if usa_cineco:
                    descuento_cineco = total * 0.10
                    total -= descuento_cineco

                total_pagar = f"${total:.2f}"

                resumen_compra = {
                    "nombre": nombre,
                    "cantidad_boletos": cantidad_boletos,
                    "tarjeta_cineco": "Sí" if usa_cineco else "No",
                    "total_pagar": total_pagar
                }

        except ValueError:
            flash("Por favor, ingresa valores numéricos válidos.", "danger")

    return render_template("cinepolis.html", total_pagar=total_pagar, resumen_compra=resumen_compra)

# Ejecutar la aplicación en modo debug en el puerto 3000
if __name__ == "__main__":
    app.run(debug=True, port=3000)


