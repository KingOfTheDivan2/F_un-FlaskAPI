from flask import Blueprint, request
from app.utils.jwt_utils import jwt_required, admin_required
from app.controllers.team_controllers import (
    create_team_controller,
    get_all_teams_controller,
    get_team_controller,
    update_team_controller,
    patch_team_controller,
    delete_team_controller
)

team_bp = Blueprint("team_bp", __name__, url_prefix="/teams")

@team_bp.route("/", methods=["POST"])
#@admin_required
def create_team():
    return create_team_controller()

@team_bp.route("/", methods=["GET"])
#@jwt_required
def get_all_teams():
    return get_all_teams_controller()

@team_bp.route("/<int:id>", methods=["GET"])
#@jwt_required
def get_team(id: int):
    return get_team_controller(id)

@team_bp.route("/<int:id>", methods=["PUT"])
#@admin_required
def update_team(id: int):
    return update_team_controller(id)

@team_bp.route("/<int:id>", methods=["PATCH"])
#@admin_required
def patch_team(id: int):
    return patch_team_controller(id)

@team_bp.route("/<int:id>", methods=["DELETE"])
#@admin_required
def delete_team(id: int):
    return delete_team_controller(id)