---
base: "[[Introduccion al Desarrollo de Software.base]]"
Fecha: 2025-05-28T22:58:00
Descripción: Algunas cosas sobre Flask, Request, JSON, …
Diapos: []
---
# Request

# Unittest

# Analisis y Explicacion de Codigo

```python
from flask import Flask, jsonify, request
import unittest

app = Flask(__name__)

def interes_compuesto(capital_inicial, tasa, anios):
    if (capital_inicial < 0 or tasa < 0 or anios < 0):
        raise ValueError("Los parámetros deben ser mayores o iguales a cero.")
    else:
        return capital_inicial * (1 + tasa) ** anios

@app.route('/interes', methods = ['POST'])
def interes():
    body_request = request.get_json()

    parametros_esperados = ["capital_inicial", "tasa", "anios"]
    for parametro in parametros_esperados:
        if parametro not in parametros_esperados:
            return jsonify({"error": f"Falta el parametro {parametro}"}), 400

        if not str(body_request[parametro].isnumeric()):
            return jsonify({"error": f"Falta el parametro {parametro}"}), 400
        
        monto_inicial = float(body_request["capital_inicial"])
        tasa = float(body_request["tasa"])
        anios = float(body_request["anios"])

        try:
            monto_final = interes_compuesto(monto_inicial, tasa, anios)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        
        return jsonify({"monto_final": monto_final})


class TestInteresCompuesto(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_calculo_correcto(self):
        resultado = round(interes_compuesto(1000, 0.05, 5), 2)
        self.assertEqual(1276.28, resultado)
  

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
```

### ✅ 1. Función `interes_compuesto(...)`

### ✅ 2. Ruta `/interes` y método `POST`

### 🧐 3. `body_request = request.get_json()`

### ⚠️ 4. El `for` que verifica los parámetros

### ✅ 5. Conversión de tipos y cálculo

### ✅ 6. Clase de test
