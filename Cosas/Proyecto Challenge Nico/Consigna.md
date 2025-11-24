---

---
# Gestión de Socios

## Registro de socio titular

**Como** administrador, **Quiero** registrar los datos personales, de contacto y domicilio de un nuevo socio.

**Para** tener un registro completo y actualizado del socio titular.

## Gestión de grupo familiar

**Como** administrador, **Quiero** agregar integrantes al grupo familiar de un socio titular.

**Para** vincular a todos los miembros bajo una misma unidad familiar.

## Edición de datos del socio o grupo familiar

**Como** administrador, **Quiero** editar los datos personales y de contacto de un socio o integrante del grupo familiar.

**Para** mantener actualizada la información de los miembros.

---

# Actividades deportivas

## Registro de actividades deportivas

**Como** administrador, **Quiero** asignar una o más actividades deportivas a un socio o miembro de grupo familiar.

**Para** saber en qué disciplinas participa cada uno.

## Visualización de actividades por socio

**Como** socio, **Quiero** ver las actividades deportivas en las que estoy inscripto yo o mi grupo familiar.

**Para** mantenerme informado de nuestra participación.

---

# Cuotas y parametrización

## Parametrización de valores de cuota

**Como** administrador, **Quiero** definir y modificar el valor de la cuota para socio simple y grupo familiar.

 **Para** ajustar fácilmente los valores en función de necesidades institucionales.

## Parametrización por edad

**Como** administrador, **Quiero** definir tramos de edad que modifiquen el valor de la cuota.

**Para** aplicar tarifas diferenciadas según la edad de los socios.

## Cálculo automático de cuota

**Como** sistema, **Quiero** calcular automáticamente el valor de la cuota según tipo de socio y edad.

**Para** garantizar una facturación coherente y sin errores manuales.

---

# Autenticación de usuarios

## Primer ingreso de socio

**Como** socio, **Quiero** ingresar con mi número de documento y establecer una nueva contraseña.

**Para** acceder por primera vez a la plataforma de forma segura.

## Encriptación de contraseña

**Como** sistema, **Quiero** encriptar la contraseña del socio con SHA1 antes de guardarla.

**Para** proteger la información sensible del usuario.

## Inicio de sesión

**Como** socio, **Quiero** ingresar a la plataforma con mi número de documento y contraseña.

**Para** acceder a mis datos y funcionalidades del sistema.

---

# Administración general

## Búsqueda de socios

**Como** administrador, **Quiero** buscar socios por nombre, documento o actividad.

**Para** acceder rápidamente a sus registros.

## Visualización de ficha completa del socio

**Como** administrador, **Quiero** ver una ficha con toda la información del socio y su grupo familiar.

**Para** tener una visión integral de su situación.

---

# Especificaciones tecnológicas

- **Frontend:** Angular 19
- **Backend:** NetCore 8
- **Base de datos:** MS-SQL 2019 o superior

**Importante:** Validar modelo entidad relación (DER).