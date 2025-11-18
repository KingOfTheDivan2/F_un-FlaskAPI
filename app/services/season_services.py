from app.models import db, Season

#region GET

def get_all_seasons() -> list[Season]:
    return Season.query.all()

def get_season_by_id(id: int) -> Season | None:

    season: Season = Season.query.filter_by(id=id).first()
    if not season:
        return None
    return season

# endregion

# region POST

def create_season(
    year: int,
    is_current: bool,
    start_date: str,
    end_date: str,
) -> Season:
    new_season = Season(
        year=year,
        is_current=is_current,
        start_date=start_date,
        end_date=end_date
    )
    db.session.add(new_season)
    db.session.commit()
    return new_season

# endregion

# region PATCH

def patch_season(id : int, data : dict) -> Season | None:

    season = get_season_by_id(id)
    if not season:
        return None
    
    if 'year' in data:
        season.year = data['year']
    if 'is_current' in data:
        season.is_current = data['is_current']
    if 'start_date' in data:
        season.start_date = data['start_date']
    if 'end_date' in data:
        season.end_date = data['end_date']
    db.session.commit()
    return season

# endregion

# region PUT

def put_driver(
    id: int,
    year: int,
    is_current: bool,
    start_date: str,
    end_date: str
) -> Season | None:
    
    season_update = get_season_by_id(id)
    if not season_update:
        return None
    
    fields = {
        "year": year,
        "is_current": is_current,
        "start_date": start_date,
        "end_date": end_date
    }

    for field, value in fields.items():
        setattr(season_update, field, value)
    db.session.commit()
    return season_update

# endregion 

# region DELETE

def delete_season(id: int) -> bool:

    season = get_season_by_id(id)
    if not season:
        return False
    db.session.delete(season)
    db.session.commit()
    return True

# endregion