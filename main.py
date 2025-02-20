from flask import Flask, render_template, request, flash, jsonify
from flask import Flask, render_template, request
from datetime import datetime
from forms import UserForm


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




#  ------------------------------------------------------------------------------------------------------------------



# Mapeo correcto de signos según el ciclo de 12 años
zodiac_years = {
    "Rata": [1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020],
    "Buey": [1913, 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    "Tigre": [1914, 1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022],
    "Conejo": [1915, 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011],
    "Dragón": [1916, 1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012],
    "Serpiente": [1917, 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025],
    "Caballo": [1918, 1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014],
    "Cabra": [1919, 1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015],
    "Mono": [1920, 1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016],
    "Gallo": [1921, 1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017],
    "Perro": [1922, 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018],
    "Cerdo": [1923, 1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019]
}

# Mapear nombres de signos a imágenes existentes en /static/img/
zodiac_map = {
    "Rata": "rata.png",
    "Buey": "bufalo.png",
    "Tigre": "tigre.png",
    "Conejo": "conejo.png",
    "Dragón": "dragon.png",
    "Serpiente": "serpiente.png",
    "Caballo": "caballo.png",
    "Cabra": "cabra.png",
    "Mono": "mono.png",
    "Gallo": "gallo.png",
    "Perro": "perro.png",
    "Cerdo": "chancho.png"
}

def calcular_edad(dia, mes, anio):
    """Calcula la edad basada en la fecha de nacimiento completa."""
    fecha_nacimiento = datetime(int(anio), int(mes), int(dia))
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nacimiento.year
    
    # Ajustar edad si aún no ha cumplido años en el año actual
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad

def obtener_signo_chino(anio):
    """Obtiene el signo zodiacal chino usando el diccionario correcto."""
    for signo, years in zodiac_years.items():
        if int(anio) in years:
            return signo, zodiac_map[signo]
    return "Desconocido", ""

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    resultado = None
    
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        apellido_paterno = request.form.get("apellido_paterno", "").strip()
        apellido_materno = request.form.get("apellido_materno", "").strip()
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        anio = request.form.get("anio")
        sexo = request.form.get("sexo")

        if not (nombre and apellido_paterno and apellido_materno and dia and mes and anio and sexo):
            resultado = "Todos los campos son obligatorios."
        else:
            edad = calcular_edad(dia, mes, anio)
            signo, imagen_nombre = obtener_signo_chino(anio)
            imagen = f"/static/img/{imagen_nombre}" if imagen_nombre else ""

            resultado = {
                "nombre": f"{nombre} {apellido_paterno} {apellido_materno}",
                "edad": edad,
                "signo": signo,
                "sexo": "Masculino" if sexo == "M" else "Femenino",
                "imagen": imagen
            }
    
    return render_template("zodiaco.html", resultado=resultado)







#-------------------------------





app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    mat = ''
    nom = ''
    ape = ''
    email = ''

    alumno_clas = UserForm(request.form)

    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data

    return render_template("Alumnos.html", form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)










if __name__ == "__main__":
    app.run(debug=True, port=3000)



