from flask import Flask, jsonify, request
from db import obtener_personas, insertar_persona, actualizar_persona, eliminar_persona

app = Flask(__name__)

@app.route("/")
def main():
    return jsonify({"mensaje": "API REST con Flask"})

@app.route("/users", methods=["GET"])
def get_users():
    datos = obtener_personas()
    lista = []

    for fila in datos:
        lista.append({
            "id": fila[0],
            "nombre": fila[1],
            "apellido": fila[2]
        })

    return jsonify(lista), 200

@app.route("/users", methods=["POST"])
def post_user():
    data = request.json

    if not data:
        return jsonify({"error": "Debes enviar un JSON"}), 400

    if "nombre" not in data or "apellido" not in data:
        return jsonify({"error": "Faltan campos: nombre y apellido"}), 400

    insertar_persona(data["nombre"], data["apellido"])

    return jsonify({
        "mensaje": "Usuario creado correctamente",
        "usuario": {
            "nombre": data["nombre"],
            "apellido": data["apellido"]
        }
    }), 201

@app.route("/users/<id>", methods=["PUT"])
def put_user(id):
    data = request.json

    if not data:
        return jsonify({"error": "Debes enviar un JSON"}), 400

    if "nombre" not in data or "apellido" not in data:
        return jsonify({"error": "Faltan campos: nombre y apellido"}), 400

    actualizar_persona(id, data["nombre"], data["apellido"])

    return jsonify({
        "mensaje": "Usuario actualizado correctamente",
        "usuario": {
            "id": id,
            "nombre": data["nombre"],
            "apellido": data["apellido"]
        }
    }), 200

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    eliminar_persona(id)

    return jsonify({
        "mensaje": "Usuario eliminado correctamente",
        "id": id
    }), 200

@app.errorhandler(404)
def no_encontrado(e):
    return jsonify({"error": "Ruta no encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
