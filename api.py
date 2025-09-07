from flask import Flask, jsonify, request
from mascota_base import ControlMascota

app = Flask(__name__)

mascota_control = ControlMascota()

# listar las mascotas
@app.route("/mascotas", methods=["GET"])
def listar_mascotas():
    return jsonify([vars(m) for m in mascota_control.listar()])                                 

@app.route("/mascotas/<int:id>", methods=["GET"])
def obtener_mascota(id):
    m = mascota_control.obtener_por_id(id)
    if m:
        return jsonify(vars(m))
    return { "error": "Mascota no encontrada" }, 401

#agregar mascotas
@app.route("/mascotas", methods=["POST"])
def agregar_mascota():
    data = request.get_json()
    nueva = mascota_control.agregar(data["nombre"], data["tipo"])
    return jsonify(vars(nueva)), 201

#modifcar mascota
@app.route("/mascotas/<int:id>", methods=["PUT"])
def modificar_mascota(id):
    data = request.get_json()
    modificada = mascota_control.modificar(id, data.get("nombre"), data.get("tipo"))
    if modificada:
        return jsonify(vars(modificada)), 201
    return { "error": "Mascota no encontrada" }, 401

#eliminar la mascota
@app.route("/mascotas/<int:id>", methods=["DELETE"])
def elimar_mascota(id):
    exito = mascota_control.eliminar(id)
    if exito:
        return { "mensaje": "Mascota eliminada con exito" }, 201
    return { "error": "Mascota no encontrada" }, 401

@app.route("/")
def inicio():
    return "Hola estudiantes de sistemas"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)