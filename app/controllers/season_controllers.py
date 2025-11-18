from app.models import db, Season
from app.services.season_services import (
    get_all_seasons,
    get_season_by_id,
    create_season,
    patch_season,
    put_driver,
    delete_season
)
from app.dto.season_dto import (
    SeasonCreateDTO,
    SeasonPatchDTO,
    SeasonUpdateDTO
)
from flask import request, jsonify

#region GET
def get_all_seasons_controller():
    """Endpoint : GET /seasons"""

    seasons = get_all_seasons()
    payload = [season.to_dict() for season in seasons]
    return jsonify(payload), 200

def get_season_by_id_controller(id : int):
    """Endpoint : GET /seasons/<id>"""

    season = get_season_by_id(id)

    if (season):
        return jsonify(season.to_dict()), 200
    return jsonify({"error" : "Season not found"}), 404
# endregion

# region POST
def create_season_controller():
    """Endpoint : POST /seasons"""
    data = request.get_json()

    dto, err = SeasonCreateDTO.from_json(data)
    if err:
        return jsonify(err), 400
    new_season = create_season(
        dto.year,
        dto.is_current,
        dto.start_date,
        dto.end_date
    )
    return jsonify(new_season.to_dict()), 201
# endregion

# region PUT
def update_season_controller(id : int):
    """Endpoint : PUT /seasons/<id>"""

    dto, err = SeasonUpdateDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    updated_season = put_driver(
        id,
        dto.year,
        dto.is_current,
        dto.start_date,
        dto.end_date
    )
    if not updated_season:
        return jsonify({"error": f"Season with id {id} not found"}), 404
    
    return jsonify(updated_season.to_dict()), 200
# endregion

# region PATCH
def patch_season_controller(id : int):
    """Endpoint : Patch /seasons/<id>"""

    dto, err = SeasonPatchDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    update_data = {k: v for k, v in dto.__dict__.items() if v is not None}
    updated = patch_season(id, update_data)
    if not updated:
        return jsonify({"error": f"Season with id {id} not found"}), 404
    
    return jsonify(updated.to_dict()), 200
# endregion

# region DELETE
def delete_season_controller(id : int):
    """Endpoint : DELETE /seasons/<id>"""
    deleted = delete_season(id)
    if deleted:
        return "", 204
    return jsonify({"error": f"Season with id {id} not found"}), 404
# endregion