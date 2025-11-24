---

---
Rutas:

- `/prendas` : me trae todas las prendas (de la tabla de prendas)
    - `/<nombre>` : me trae esa prenda en especifico (con toda su info “JOINEADA”) (acepta put y delete)
        - `/stock` : me trae el stock de esa prenda
- `/talles` : me trae todos los talles (acepta post, put y delete)
- `/colores` : me trae todos los colores (acepta post, put y delete)
- `/clientes` : me trae todos los clientes
    - `/<id> o <nombre>` : me trae un cliente (acepta put y delete)
        - `/compras` : me trae el historial de compra de ese cliente
