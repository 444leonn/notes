---
base: "[[Introduccion al Desarrollo de Software.base]]"
Fecha: 2025-05-28T22:58:00
Descripción: ""
Diapos: []
---
# Una Aplicacion Sencilla

Toda aplicacion minima de Flask comienza con el siguiente codigo.

```python
from flask import Flask # 1

app = Flask(__name__) # 2

@app.route("/") # 3
def hello_world(): # 4
    return "<p>Hello, World!</p>"
```

Pero, que es lo que hace exactamente este codigo?

# API