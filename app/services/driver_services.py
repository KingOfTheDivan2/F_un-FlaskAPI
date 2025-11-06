from app.models import db, Driver

# region GET

def get_all_drivers() -> list[Driver]:
    return Driver.query.all()

def get_driver_by_id(id: int) -> Driver | None:

    driver: Driver = Driver.query.filter_by(id=id).first()
    if not driver:
        return None
    return driver

# endregion

# region Post

def create_driver(
    driver_ref: str,
    first_name: str,
    last_name: str,
    nationality: str,
    birth_date: str,
    is_actual_champion: bool,
    is_using_number_one: bool,
    car_number: int,
    team_id: int,
    total_points: float = 0,
    total_wins: int = 0,
    total_podiums: int = 0,
    number_championship_won: int = 0,
    image: str | None = None
) -> Driver:
    new_driver = Driver(
        driver_ref=driver_ref,
        first_name=first_name,
        last_name=last_name,
        nationality=nationality,
        birth_date=birth_date,
        is_actual_champion=is_actual_champion,
        is_using_number_one=is_using_number_one,
        car_number=car_number,
        team_id=team_id,
        total_points=total_points,
        total_wins=total_wins,
        total_podiums=total_podiums,
        number_championship_won=number_championship_won,
        image=image
    )
    db.session.add(new_driver)
    db.session.commit()
    return new_driver

# endregion

# region PATCH

def patch_driver(id : int, data : dict) -> Driver | None:

    driver = get_driver_by_id(id)
    if not driver:
        return None
    
    if 'driver_ref' in data:
        driver.driver_ref = data['driver_ref']
    if 'first_name' in data:
        driver.first_name = data['first_name']
    if 'last_name' in data:
        driver.last_name = data['last_name']
    if 'nationality' in data:
        driver.nationality = data['nationality']
    if 'birth_date' in  data:
        driver.birth_date = data['birth_date']
    if 'is_actual_champion' in data:
        driver.is_actual_champion = data['is_actual_champion']
    if 'car_number' in data:
        driver.car_number = data['car_number']
    if 'team_id' in data:
        driver.team_id = data['team_id']
    if 'total_points' in data:
        driver.total_points = data['total_points']
    if 'total_wins' in data:
        driver.total_wins = data['total_wins']
    if 'total_podiums' in data:
        driver.total_podiums = data['total_podiums']
    if 'number_championship_won' in data:
        driver.number_championship_won = data['number_champioship_won']
    if 'image' in data:
        driver.image = data['image']
    db.session.commit()
    return driver

# endregion

# region PUT

def put_driver(
    id: int,
    driver_ref: str,
    first_name: str,
    last_name: str,
    nationality: str,
    birth_date: str,
    is_actual_champion: bool,
    is_using_number_one: bool,
    car_number: int,
    team_id: int,
    total_points: float = 0,
    total_wins: int = 0,
    total_podiums: int = 0,
    number_championship_won: int = 0,
    image: str | None = None
) -> Driver | None:

    driver_update = get_driver_by_id(id)
    if not driver_update:
        return None
    
    fields = {
        "driver_ref": driver_ref,
        "first_name": first_name,
        "last_name": last_name,
        "nationality": nationality,
        "birth_date": birth_date,
        "is_actual_champion": is_actual_champion,
        "is_using_number_one": is_using_number_one,
        "car_number": car_number,
        "team_id": team_id,
        "total_points": total_points,
        "total_wins": total_wins,
        "total_podiums": total_podiums,
        "number_championship_won": number_championship_won,
        "image": image
    }

    for field, value in fields.items():
        setattr(driver_update, field, value)
    db.session.commit()
    return driver_update

# endregion

# region DELETE

def delete_driver(id: int) -> bool:

    driver = get_driver_by_id(id)
    if not driver:
        return False
    db.session.delete(driver)
    db.session.commit()
    return True

# endregion