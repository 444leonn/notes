---

---
Fecha de entrega: 10/04/2025 | Clase Presencial y Obligatoria | Individual o en Grupos de hasta 3 personas

La cafetería *Ghirardelli* nos ha solicitado desarrollar una página web para su sucursal enDisney Springs. Un diseñador nos ha proporcionado una plantilla de interfaz de usuariointuitiva, y nuestra tarea es dotarla de dinamismo y funcionalidad según losrequerimientos del café. Además, el hijo del dueño, apasionado por la programación,nos ha proporcionado las siguientes pautas para la implementación del sitio web.

**Requerimientos:**

1. Crear un script en bash que al ejecutarlo cree un proyecto en flask llamado “EjPractico2” con el ambiente virtual, y un archivo (vacío) [app.py](http://app.py/). El proyecto deberá tener las carpetas abajo mencionadas:.
└── /TP2-IDS/
2. Crear un archivo base.html, que reutilice todo el código posible (que se encuentra repetido en las distintas páginas html).
3. Referenciar el contenido del template a la cafetería de interés (todas lasapariciones de “Brooklyn” deberán ser reemplazadas por “Ghirardelli”). Utilizar una variable.
4. Reemplazar todas las urls por url-for según corresponda.
5. Reparar la redirección de los archivos que sean invocados dentro del código HTML.
*Ejemplo:*
6. Colocar imágenes de platos y comidas, obtenidas de la web en forma gratuita,reemplazando las existentes en el template.
*Ejemplo:*
7. Crear una variable tipo diccionario que contenga toda la información de losplatos.
*Ejemplo:*
8. Modificar el archivo style.css de forma tal que el diseño del template (que esoscuro) sea claro, al igual que el sitio oficial de “Ghirardelli”. Para esto se deberán modificar los colores de los textos y el color de fondo del sitio web.
9. Modificar el form de la página de contacto para que, al clickear en el botón deenvío de información, se envíe un correo electrónico con el cuerpo del formulario(el contacto del usuario).
Para implementar el envío de correos electrónicos, pueden utilizar el siguientecódigo como ejemplo
```html
rom flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'

app.config['MAIL_PORT'] = 587

app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USE_SSL'] = False

app.config['MAIL_USERNAME'] = 'your-email@gmail.com'

app.config['MAIL_PASSWORD'] = 'your-email-password' security

app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

mail = Mail(app)
```