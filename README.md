# API REST con Flask y SQLite

## Descripción
Este proyecto implementa una API REST utilizando Flask y SQLite.  
La API gestiona un recurso llamado **user**, permitiendo operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

El objetivo es demostrar la construcción estructurada de una API, manejo de rutas, validaciones, respuestas en formato JSON y pruebas a través de Postman.

---

## Objetivos del Proyecto
- Diseñar e implementar una API REST funcional.
- Utilizar Flask como microframework para construir servicios web.
- Persistir datos mediante SQLite sin necesidad de un servidor adicional.
- Aplicar buenas prácticas de arquitectura y organización del código.
- Probar endpoints mediante herramientas como Postman.

---

## Estructura del Proyecto

---

## Tecnologías Utilizadas
- **Python 3.9+**
- **Flask**
- **SQLite3**
- **Postman** para pruebas

---

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuproject/api_flask_sqlite.git
cd api_flask_sqlite

### 2. Crear un entorno virtual
python -m venv venv

venv\Scripts\activate   
-- structureDB.sql
PRAGMA foreign_keys = ON;


### 3. Crear el archivo structureDB.sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT,


4. Crear db.py

Implementa las funciones:
get(id=None)
post(data)
put(id, data)
delete(id)

Incluye manejo de errores y validaciones

### 5. Crear app.py

Contiene:
Las rutas de usuarios.
Respuestas JSON.
Validaciones.
Códigos de error HTTP.

### 6. Ejecutar la API

python app.py

### 7. URL base
http://127.0.0.1:5000

Base de Datos

La base de datos SQLite se genera automáticamente al iniciar el proyecto por primera vez.

Endpoints Disponibles
Obtener todos los usuarios

GET /users

Obtener un usuario por ID

GET /users/<id>

Crear un usuario

POST /users

Ejemplo:

{
  "nombre": "Carlos",
  "apellido": "Barrera",
  "id": 1
}

Actualizar usuario

PUT /users/<id>

Eliminar usuario

DELETE /users/<id>

Pruebas con Postman
Pruebas GET en Postman
GET /users — Obtener todos los usuarios

Método: GET
Endpoint: http://127.0.0.1:5000/users


GET /users/<id> — Obtener usuario por ID

Método: GET
Endpoint: http://127.0.0.1:5000/users/8


Error GET — ID no existente

Método: GET
Endpoint: http://127.0.0.1:5000/users/1


Pruebas POST
POST /users — Crear un nuevo usuario

Método: POST
Endpoint: http://127.0.0.1:5000/users


Error POST — email duplicado

Error POST — faltan datos

Pruebas PUT
PUT /users/<id> — Actualizar un usuario

Método: PUT
Endpoint: http://127.0.0.1:5000/users/8




Error PUT — ID no existente

Pruebas DELETE
DELETE /users/<id> — Eliminar un usuario

Método: DELETE
Endpoint: http://127.0.0.1:5000/users/9




Error DELETE — ID no existente