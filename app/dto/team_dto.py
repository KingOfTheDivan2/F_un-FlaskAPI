from dataclasses import dataclass, field
from app.utils.verify_utils import VerifyTeamUtils

from typing import Optional, Tuple, Dict

@dataclass
class TeamCreateDTO:
    name: str
    country: str
    address: str
    team_principal: str
    founded_year: int
    total_points: Optional[float] = field(default=0)
    total_wins: Optional[int] = field(default=0)
    championships_won: Optional[int] = field(default=0)
    is_actual_champion: Optional[bool] = field(default=False)
    logo_url: Optional[str] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['TeamCreateDTO'], Optional[Dict]]:

        if not data:
            return None, {"error": "No data provided"}
        
        # === Extracting data | Normalization removing spaces ===

        name = (data.get('name') or "").strip()
        country = (data.get('country') or "").strip()
        address = (data.get('address') or "").strip()
        team_principal = (data.get('team_principal') or "").strip()
        founded_year = data.get('founded_year')
        total_points = data.get('total_points', 0)
        total_wins = data.get('total_wins', 0)
        championships_won = data.get('championships_won', 0)
        is_actual_champion = data.get('is_actual_champion', False)
        logo_url = (data.get('logo_url') or "").strip() or None

        # === Required fields ===

        required_fields = {
            'name': name,
            'country': country,
            'address': address,
            'team_principal': team_principal,
            'founded_year': founded_year
        }
        for field, value in required_fields.items():
            if value in [None, '']:
                return None, {"error": f"Missing field: {field}"}
            
        # === Validations ===

        if not VerifyTeamUtils.is_valid_name(name):
            return None, {"error": "Invalid name"}
        
        if not VerifyTeamUtils.is_valid_country(country):
            return None, {"error": "Invalid country"}
        
        if not VerifyTeamUtils.is_valid_address(address):
            return None, {"error": "Invalid address"}
        
        if not VerifyTeamUtils.is_valid_team_principal(team_principal):
            return None, {"error": "Invalid team principal"}
        
        if not VerifyTeamUtils.is_valid_founded_year(founded_year):
            return None, {"error": "Invalid founded year"}
        
        if not VerifyTeamUtils.is_valid_total_points(total_points):
            return None, {"error": "Invalid total points"}
        
        if not VerifyTeamUtils.is_valid_total_wins(total_wins):
            return None, {"error": "Invalid total wins"}
        
        if not VerifyTeamUtils.is_valid_championships_won(championships_won):
            return None, {"error": "Invalid championships won"}
        
        if not VerifyTeamUtils.is_valid_is_actual_champion(is_actual_champion):
            return None, {"error": "Invalid is actual champion"}
        
        if not VerifyTeamUtils.is_valid_logo_url(logo_url):
            return None, {"error": "Invalid logo URL"}
        
        return TeamCreateDTO(
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
        ), None
    
@dataclass
class TeamUpdateDTO:
    name : str
    country : str
    address : str
    team_principal : str
    founded_year : int
    total_points : Optional[float] = field(default=0)
    total_wins : Optional[int] = field(default=0)
    championships_won : Optional[int] = field(default=0)
    is_actual_champion : Optional[bool] = field(default=False)
    logo_url : Optional[str] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['TeamUpdateDTO'], Optional[Dict]]:
        
        if not data:
            return None, {"error": "Data missing for complete update"}
        
        dto, err = TeamCreateDTO.from_json(data)

        if err:
            return None, err
        
        return TeamUpdateDTO(
            name=dto.name,
            country=dto.country,
            address=dto.address,
            team_principal=dto.team_principal,
            founded_year=dto.founded_year,
            total_points=dto.total_points,
            total_wins=dto.total_wins,
            championships_won=dto.championships_won,
            is_actual_champion=dto.is_actual_champion,
            logo_url=dto.logo_url
        ), None
    
@dataclass
class TeamPatchDTO:
    name: Optional[str] = field(default=None)
    country: Optional[str] = field(default=None)
    address: Optional[str] = field(default=None)
    team_principal: Optional[str] = field(default=None)
    founded_year: Optional[int] = field(default=None)
    total_points: Optional[float] = field(default=None)
    total_wins: Optional[int] = field(default=None)
    championships_won: Optional[int] = field(default=None)
    is_actual_champion: Optional[bool] = field(default=None)
    logo_url: Optional[str] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['TeamPatchDTO'], Optional[Dict]]:
        if not data:
            return None, {"error": "No data provided for patching"}
        
        name = data.get('name')
        country = data.get('country')
        address = data.get('address')
        team_principal = data.get('team_principal')
        founded_year = data.get('founded_year')
        total_points = data.get('total_points')
        total_wins = data.get('total_wins')
        championships_won = data.get('championships_won')
        is_actual_champion = data.get('is_actual_champion')
        logo_url = data.get('logo_url')

        if all(v is None for v in [name, country, address, team_principal, founded_year, total_points, total_wins, championships_won, is_actual_champion, logo_url]):
            return None, {"error": "No fields provided for patch"}
        
        if name is not None and not VerifyTeamUtils.is_valid_name(name):
            return None, {"error": "Invalid name"}
        
        if country is not None and not VerifyTeamUtils.is_valid_country(country):
            return None, {"error": "Invalid country"}
        
        if address is not None and not VerifyTeamUtils.is_valid_address(address):
            return None, {"error": "Invalid address"}
        
        if team_principal is not None and not VerifyTeamUtils.is_valid_team_principal(team_principal):
            return None, {"error": "Invalid team principal"}
        
        if founded_year is not None and not VerifyTeamUtils.is_valid_founded_year(founded_year):
            return None, {"error": "Invalid founded year"}

        if total_points is not None and not VerifyTeamUtils.is_valid_total_points(total_points):
            return None, {"error": "Invalid total of points"}
        
        if total_wins is not None and not VerifyTeamUtils.is_valid_total_wins(total_wins):
            return None, {"error": "Invalid total of wins"}
        
        if championships_won is not None and not VerifyTeamUtils.is_valid_championships_won(championships_won):
            return None, {"error": "Invalid number of championships won"}
        
        if is_actual_champion is not None and not VerifyTeamUtils.is_valid_is_actual_champion(is_actual_champion):
            return None, {"error": "Invalid actual champion status"}
        
        if logo_url is not None and not VerifyTeamUtils.is_valid_logo_url(logo_url):
            return None, {"error": "Invalid logo url"}
        
        return TeamPatchDTO(
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
        ), None

