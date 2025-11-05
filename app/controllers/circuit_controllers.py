from app.models import db, Circuit
from app.services.circuit_service import (
    get_all_circuits,
    get_circuit_by_id,
    create_circuit,
    patch_circuit,
    put_circuit,
    delete_circuit
)
from app.dto.circuit_dto import (
    CircuitCreateDTO,
    CircuitUpdateDTO,
    CircuitPatchDTO
)
from flask import request, jsonify

# region GET
def get_circuit_controller(id : int):
    """Endpoint : GET /api/circuit/<id>"""

    circuit = get_circuit_by_id(id)

    if (circuit):
        return jsonify(circuit.to_dict()), 200
    return jsonify({"error": "Circuit not found"}), 404

def get_all_circuits_controller():
    """Endpoint : GET /api/circuits"""

    circuits = get_all_circuits()
    payload = [circuit.to_dict() for circuit in circuits]
    return jsonify(payload), 200
# endregion

# region POST
def create_circuit_controller():
    """Endpoint : POST /api/circuit"""
    data = request.get_json()

    dto, err = CircuitCreateDTO.from_json(data)
    if err:
        return jsonify(err), 400
    
    new_circuit = create_circuit(
        dto.name,
        dto.city,
        dto.country,
        dto.first_grand_prix_year,
        dto.length_km,
        dto.number_of_laps,
        dto.fastest_lap_time
    )
    return jsonify(new_circuit.to_dict()), 201
# endregion

# region PUT
def update_circuit_controller(id : int):
    """Endpoint : PUT /api/circuit/<id>"""

    dto, err = CircuitUpdateDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    updated_circuit = put_circuit(
        id,
        dto.name,
        dto.city,
        dto.country,
        dto.first_grand_prix_year,
        dto.length_km,
        dto.number_of_laps,
        dto.fastest_lap_time
    )
    if not updated_circuit:
        return jsonify({"error": f"Circuit with id {id} not found"}), 404
    
    return jsonify(updated_circuit.to_dict()), 200
# endregion

# region PATCH
def patch_circuit_controller(id : int):
    """Endpoint : PATCH /api/circuit/<id>"""

    dto, err = CircuitPatchDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    update_data = {k: v for k, v in dto.__dict__.items() if v is not None}

    updated = patch_circuit(id, update_data)
    if not updated:
        return jsonify({"error": f"Circuit with id {id} not found"}), 404
    
    return jsonify(updated.to_dict()), 200
# endregion

# region DELETE
def delete_circuit_controller(id : int):
    """Endpoint : DELETE /api/circuit/<id>"""
    deleted = delete_circuit(id)
    if deleted:
        return "", 204
    return jsonify({"error": f"Circuit with id {id} not found"}), 404
# endregion