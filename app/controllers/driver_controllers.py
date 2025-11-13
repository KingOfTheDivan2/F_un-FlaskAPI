from app.models import db, Driver
from app.services.driver_services import (
    get_all_drivers,
    get_driver_by_id,
    create_driver,
    patch_driver,
    put_driver,
    delete_driver
)
from app.dto.driver_dto import (
    DriverCreateDTO,
    DriverPatchDTO,
    DriverUpdateDTO
)
from flask import request, jsonify

# region GET
def get_all_drivers_controller():
    """Endpoint : GET /drivers"""

    drivers = get_all_drivers()
    payload = [driver.to_dict() for driver in drivers]
    return jsonify(payload), 200

def get_driver_by_id_controller(id : int):
    """Endpoint : GET /drivers/<id>"""

    driver = get_driver_by_id(id)

    if (driver):
        return jsonify(driver.to_dict()), 200
    return jsonify({"error": "Driver not found"}), 404
# endregion

# region POST
def create_driver_controller():
    """Endpoint : POST /drivers"""
    data = request.get_json()

    dto, err = DriverCreateDTO.from_json(data)
    if err:
        return jsonify(err), 400
    new_driver = create_driver(
        dto.driver_ref,
        dto.first_name,
        dto.last_name,
        dto.nationality,
        dto.birth_date,
        dto.is_actual_champion,
        dto.is_using_number_one,
        dto.car_number,
        dto.team_id,
        dto.total_points,
        dto.total_wins,
        dto.total_podiums,
        dto.number_championship_won,
        dto.image
    )
    return jsonify(new_driver.to_dict()), 201
# endregion

# region PUT
def update_driver_controller(id : int):
    """Endpoint : PUT /drivers/<id>"""

    dto, err = DriverUpdateDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    updated_driver = put_driver(
        id,
        dto.driver_ref,
        dto.first_name,
        dto.last_name,
        dto.nationality,
        dto.birth_date,
        dto.is_actual_champion,
        dto.is_using_number_one,
        dto.car_number,
        dto.team_id,
        dto.total_points,
        dto.total_wins,
        dto.total_podiums,
        dto.number_championship_won,
        dto.image
    )
    if not updated_driver:
        return jsonify({"error": f"Driver with id {id} not found"}), 404
    
    return jsonify(updated_driver.to_dict()), 200
# endregion

# region PATCH
def patch_driver_controller(id : int):
    """Endpoint : PATCH /drivers/<id>"""

    dto, err = DriverPatchDTO.from_json(request.get_json())
    if err:
        return jsonify(err), 400
    
    update_data = {k: v for k, v in dto.__dict__.items() if v is not None}
    updated = patch_driver(id, update_data)
    if not updated:
        return jsonify({"error": f"Driver with id {id} not found"}), 404
    
    return jsonify(updated.to_dict()), 200
#endregion

# region DELETE
def delete_driver_controller(id : int):
    """Endpoint : DELETE /drivers/<id>"""
    deleted = delete_driver(id)
    if deleted:
        return "", 204
    return jsonify({"error": f"Driver with id {id} not found"}), 404
# endregion