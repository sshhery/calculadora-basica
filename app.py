from flask import Flask, render_template_string, request

app = Flask(__name__)  # Asegúrate de usar __name_ con dos guiones bajos

# HTML y CSS mejorado para la calculadora
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Mejorada</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        .calculator {
            display: inline-block;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input[type="text"] {
            width: 80px;
            padding: 10px;
            margin: 5px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        select {
            padding: 10px;
            margin: 5px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #28a745;
            color: white;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <h1>Calculadora Mejorada</h1>
    <div class="calculator">
        <form method="post">
            <input type="text" name="num1" placeholder="Número 1" value="{{ num1 }}">
            <select name="operation">
                <option value="sumar" {% if operation == 'sumar' %}selected{% endif %}>+</option>
                <option value="restar" {% if operation == 'restar' %}selected{% endif %}>-</option>
                <option value="multiplicar" {% if operation == 'multiplicar' %}selected{% endif %}>*</option>
                <option value="dividir" {% if operation == 'dividir' %}selected{% endif %}>/</option>
                <option value="potencia" {% if operation == 'potencia' %}selected{% endif %}>^</option>
                <option value="raiz" {% if operation == 'raiz' %}selected{% endif %}>√</option>
            </select>
            <input type="text" name="num2" placeholder="Número 2" value="{{ num2 }}">
            <input type="submit" value="Calcular">
        </form>
        {% if resultado is not none %}
            <h2>Resultado: {{ resultado }}</h2>
        {% endif %}
        {% if error is not none %}
            <h2 style="color: red;">{{ error }}</h2>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    error = None
    num1 = request.form.get("num1", "")
    num2 = request.form.get("num2", "")
    operation = request.form.get("operation", "sumar")

    try:
        if num1 and num2:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "sumar":
                resultado = num1 + num2
            elif operation == "restar":
                resultado = num1 - num2
            elif operation == "multiplicar":
                resultado = num1 * num2
            elif operation == "dividir":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    error = "Error: División por cero"
            elif operation == "potencia":
                resultado = num1 ** num2
            elif operation == "raiz":
                if num1 >= 0:
                    resultado = num1 ** (1 / num2)
                else:
                    error = "Error: La raíz de un número negativo no es válida"
        else:
            error = "Por favor, ingresa ambos números"
    except ValueError:
        error = "Error: Entrada no válida"

    return render_template_string(html_code, resultado=resultado, error=error, num1=num1, num2=num2, operation=operation)

if __name__ == "__main__":
    app.run(debug=True)