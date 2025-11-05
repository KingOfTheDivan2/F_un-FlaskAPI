from flask import Blueprint, request
from app.utils.jwt_utils import jwt_required, admin_required
from app.controllers.circuit_controllers import (
    create_circuit_controller,
    get_all_circuits_controller,
    get_circuit_controller,
    update_circuit_controller,
    patch_circuit_controller,
    delete_circuit_controller,
)

circuit_bp = Blueprint("circuit_bp", __name__, url_prefix="/circuits")

@circuit_bp.route("/", methods=["POST"])
#@admin_required
def create_circuit():
    return create_circuit_controller()

@circuit_bp.route("/", methods=["GET"])
#@jwt_required
def get_all_circuits():
    return get_all_circuits_controller()

@circuit_bp.route("/<int:id>", methods=["GET"])
#@jwt_required
def get_circuit(id: int):
    return get_circuit_controller(id)

@circuit_bp.route("/<int:id>", methods=["PUT"])
#@admin_required
def update_circuit(id: int):
    return update_circuit_controller(id)

@circuit_bp.route("/<int:id>", methods=["PATCH"])
#@admin_required
def patch_circuit(id: int):
    return patch_circuit_controller(id)

@circuit_bp.route("/<int:id>", methods=["DELETE"])
#@admin_required
def delete_circuit(id: int):
    return delete_circuit_controller(id)
