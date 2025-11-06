from app.models import db, Team
from app.services.team_services import (
    get_all_teams,
    get_team_by_id,
    create_team,
    patch_team,
    put_team,
    delete_team
)
from app.dto.team_dto import (
    TeamCreateDTO,
    TeamPatchDTO,
    TeamUpdateDTO
)
from flask import request, jsonify

# region GET
def get_all_teams_controller():
    """Endpoint : GET /teams"""

    teams = get_all_teams()
    payload = [team.to_dict() for team in teams]
    return jsonify(payload), 200

def get_team_controller(id : int):
    """Endpoint : GET /teams/<id>"""

    team = get_team_by_id(id)

    if (team):
        return jsonify(team.to_dict()), 200
    return jsonify({"error": "Team not found"}), 404
# endregion

# region POST
def create_team_controller():
    """Endpoint : POST /teams"""
    data = request.get_json()

    dto, err = TeamCreateDTO.from_json(data)
    if err:
        return jsonify(err), 400
    new_team = create_team(
        dto.name,
        dto.country,
        dto.address,
        dto.team_principal,
        dto.founded_year,
        dto.total_points,
        dto.total_wins,
        dto.championships_won,
        dto.is_actual_champion,
        dto.logo_url
    )
    return jsonify(new_team.to_dict()), 201
# endregion

# region PUT
def update_team_controller(id : int):
    """Endpoint : PUT /teams/<id>"""

    dto, err = TeamUpdateDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    updated_team = put_team(
        id,
        dto.name,
        dto.country,
        dto.address,
        dto.team_principal,
        dto.founded_year,
        dto.total_points,
        dto.total_wins,
        dto.championships_won,
        dto.is_actual_champion,
        dto.logo_url
    )
    if not updated_team:
        return jsonify({"error" : f"Team with id {id} not found"}), 404
    
    return jsonify(updated_team.to_dict()), 200
# endregion

# region PATCH
def patch_team_controller(id : int):
    """Endpoint : PATCH /teams/<id>"""

    dto, err = TeamPatchDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    update_data = {k: v for k, v in dto.__dict__.items() if v is not None}

    updated = patch_team(id, update_data)
    if not updated:
        return jsonify({"error": f"Team with id {id} not found"}), 404
    
    return jsonify(updated.to_dict()), 200
# endregion

# region DELETE
def delete_team_controller(id : int):
    """Endpoint : DELETE /teams/<id>"""
    deleted = delete_team(id)
    if deleted:
        return "", 204
    return jsonify({"error": f"Team with id {id} not found"}), 404
# endregion
