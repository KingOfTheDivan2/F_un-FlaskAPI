from flask import Blueprint, request
from app.utils.jwt_utils import jwt_required, admin_required
from app.controllers.driver_controllers import(
    create_driver_controller,
    get_all_drivers_controller,
    get_driver_by_id_controller,
    update_driver_controller,
    patch_driver_controller,
    delete_driver_controller
)

driver_bp = Blueprint("driver_bp", __name__, url_prefix="/drivers")

@driver_bp.route("/", methods=["POST"])
#@admin_required
def create_driver():
    return create_driver_controller()

@driver_bp.route("/", methods=["GET"])
#@jwt_required
def get_all_drivers():
    return get_all_drivers_controller()

@driver_bp.route("/<int:id>", methods=["GET"])
#@jwt_required
def get_driver(id : int):
    return get_driver_by_id_controller(id)

@driver_bp.route("/<int:id>", methods=["PUT"])
#@admin_required
def update_driver(id : int):
    return update_driver_controller(id)

@driver_bp.route("/<int:id>", methods=["PATCH"])
#@admin_required
def patch_driver(id : int):
    return patch_driver_controller(id)

@driver_bp.route("/<int:id>", methods=["DELETE"])
#@admin_required
def delete_driver(id : int):
    return delete_driver_controller(id)