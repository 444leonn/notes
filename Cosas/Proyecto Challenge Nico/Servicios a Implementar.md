# Servicios

Todos van precedidos de `/api`

## Socios

- `/socios` → Me trae todos los socios acepta GET, POST, PUT y DELETE
- `/socios/<id>` → Me trae un socio en especifico con **todos sus datos**, acepta GET, POST, PUT y DELETE
- `/socios/titulares` → Me trae todos los socios con un contador de cuantos adherentes tiene cada uno 
- `/socios/grupos/<id_titular>`  → Me trae el grupo familiar completo

## Tipos Socios

- `/tipos` → Me trae todos los tipos de socios
- `/tipos/<id>` → Me trae un tipo de socio en especifico

## Deportes

- `/deportes` → todos los deportes, acepta GET, POST, PUT y DELETE
- `/deportes/<id>` → un deporte en especifico, acepta GET, POST,  PUT y DELETE

---

Ver como manejar la busqueda con los query params

**SQL** Campo default value por binding GetDate()
