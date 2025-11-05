from app.models import Circuit, db


# region GET

def get_circuit_by_id(id: int) -> Circuit | None:
    """Retrieve a Circuit by its ID."""
    circuit : Circuit = Circuit.query.filter_by(id=id).first()
    if not circuit:
        return None
    return circuit

def get_all_circuits() -> list[Circuit]:
    """Retrieve all Circuits."""
    return Circuit.query.all()

# endregion

# region POST

def create_circuit(
    name: str,
    city: str,
    country: str,
    first_grand_prix_year: int,
    length_km: float,
    number_of_laps: int,
    fastest_lap_time: float | None = None
) -> Circuit:
    """Returns a created Circuit."""
    new_circuit = Circuit(
        name=name,
        city=city,
        country=country,
        first_grand_prix_year=first_grand_prix_year,
        length_km=length_km,
        number_of_laps=number_of_laps,
        fastest_lap_time=fastest_lap_time
    )
    db.session.add(new_circuit)
    db.session.commit()
    return new_circuit

# endregion

# region PATCH

def patch_circuit(id : int, data : dict) -> Circuit | None:
    """Update partial data of a Circuit."""
    circuit = get_circuit_by_id(id)
    if not circuit:
        return None
    
    if 'name' in data:
        circuit.name = data['name']
    if 'city' in data:
        circuit.city = data['city']
    if 'country' in data:
        circuit.country = data['country']
    if 'first_grand_prix_year' in data:
        circuit.first_grand_prix_year = data['first_grand_prix_year']
    if 'length_km' in data:
        circuit.length_km = data['length_km']
    if 'number_of_laps' in data:
        circuit.number_of_laps = data['number_of_laps']
    if 'fastest_lap_time' in data:
        circuit.fastest_lap_time = data['fastest_lap_time']
    db.session.commit()
    return circuit

# endregion

# region PUT

def put_circuit(
    id: int,
    name: str,
    city: str,
    country: str,
    first_grand_prix_year: int,
    length_km: float,
    number_of_laps: int,
    fastest_lap_time: float | None = None
) -> Circuit | None:
    """Fully update a Circuit."""
    circuit_update = get_circuit_by_id(id)
    if not circuit_update:
        return None
    
    fields = {
        'name': name,
        'city': city,
        'country': country,
        'first_grand_prix_year': first_grand_prix_year,
        'length_km': length_km,
        'number_of_laps': number_of_laps,
        'fastest_lap_time': fastest_lap_time
    }

    for field, value in fields.items():
        setattr(circuit_update, field, value)
    db.session.commit()
    return circuit_update

# endregion

# region DELETE

def delete_circuit(id: int) -> bool:
    """Delete a Circuit by its ID."""
    circuit = get_circuit_by_id(id)
    if not circuit:
        return False
    db.session.delete(circuit)
    db.session.commit()
    return True

# endregion