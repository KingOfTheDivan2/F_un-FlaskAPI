from app.models import db, Team

# region GET

def get_team_by_id(id: int) -> Team | None:
    """Retrieve a Team by its ID."""
    team: Team = Team.query.filter_by(id=id).first()
    if not team:
        return None
    return team

def get_all_teams() -> list[Team]:
    return Team.query.all()

# endregion

# region POST

def create_team(
    name: str,
    country: str,
    address: str,
    team_principal: str,
    founded_year: int,
    total_points: float = 0,
    total_wins: int = 0,
    championships_won: int = 0,
    is_actual_champion: bool = False,
    logo_url: str | None = None
) -> Team:
    new_team = Team(
        name=name,
        country=country,
        address=address,
        team_principal=team_principal,
        founded_year=founded_year,
        total_points=total_points,
        total_wins=total_wins,
        championships_won=championships_won,
        is_actual_champion=is_actual_champion,
        logo_url=logo_url
    )
    db.session.add(new_team)
    db.session.commit()
    return new_team

# endregion

# region PATCH

def patch_team(id : int, data : dict) -> Team | None:

    team = get_team_by_id(id)
    if not team:
        return None
    
    if 'name' in data:
        team.name = data['name']
    if 'country' in data:
        team.country = data['country']
    if 'address' in data:
        team.address = data['address']
    if 'team_principal' in data:
        team.team_principal = data['team_principal']
    if 'founded_year' in data:
        team.founded_year = data['founded_year']
    if 'total_points' in data:
        team.total_points = data['total_points']
    if 'total_wins' in data:
        team.total_wins = data['total_wins']
    if 'championships_won' in data:
        team.championships_won = data['championships_won']
    if 'is_actual_champion' in data:
        team.is_actual_champion = data['is_actual_champion']
    if 'logo_url' in data:
        team.logo_url = data['logo_url']
    db.session.commit()
    return team

# endregion

# region PUT

def put_team(
    id: int,
    name: str,
    country: str,
    address: str,
    team_principal: str,
    founded_year: int,
    total_points: float = 0,
    total_wins: int = 0,
    championships_won: int = 0,
    is_actual_champion: bool = False,
    logo_url: str | None = None
) -> Team | None:
    
    team_update = get_team_by_id(id)
    if not team_update:
        return None
    
    fields = {
        'name': name,
        'country': country,
        'address': address,
        'team_principal': team_principal,
        'founded_year': founded_year,
        'total_points': total_points,
        'total_wins': total_wins,
        'championships_won': championships_won,
        'is_actual_champion': is_actual_champion,
        'logo_url': logo_url
    }

    for field, value in fields.items():
        setattr(team_update, field, value)
    db.session.commit()
    return team_update

# endregion

# region DELETE

def delete_team(id: int) -> bool:

    team = get_team_by_id(id)
    if not team:
        return False
    db.session.delete(team)
    db.session.commit()
    return True

# endregion