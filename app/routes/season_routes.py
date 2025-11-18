from flask import Blueprint, request
from app.utils.jwt_utils import jwt_required, admin_required
from app.controllers.season_controllers import(
    create_season_controller,
    get_all_seasons_controller,
    get_season_by_id_controller,
    update_season_controller,
    patch_season_controller,
    delete_season_controller
)

season_bp = Blueprint("season_bp", __name__, url_prefix="/seasons")

@season_bp.route("/", methods=["POST"])
#@admin_required
def create_season():
    return create_season_controller()

@season_bp.route("/", methods=["GET"])
#@jwt_required
def get_all_seasons():
    return get_all_seasons_controller()

@season_bp.route("/<int:id>", methods=["GET"])
#@jwt_required
def get_season(id : int):
    return get_season_by_id_controller(id)

@season_bp.route("/<int:id>", methods=["PUT"])
#@admin_required
def update_season(id : int):
    return update_season_controller(id)

@season_bp.route("/<int:id>", methods=["PATCH"])
#@admin_required
def patch_season(id : int):
    return patch_season_controller(id)

@season_bp.route("/<int:id>", methods=["DELETE"])
#@admin_required
def delete_season(id : int):
    return delete_season_controller(id)
