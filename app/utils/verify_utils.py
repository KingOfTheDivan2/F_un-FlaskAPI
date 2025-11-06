from typing import Optional
from datetime import datetime


class VerifyCircuitUtils:
    
    @staticmethod
    def is_valid_name(name: str) -> bool:
        return isinstance(name, str) and 0 < len(name) <= 100 
    
    @staticmethod
    def is_valid_city(city: str) -> bool:
        return isinstance(city, str) and 0 < len(city) <= 100 
    
    @staticmethod
    def is_valid_country(country: str) -> bool:
        return isinstance(country, str) and  0 < len(country) <= 100 
    
    @staticmethod
    def is_valid_first_gp_year(year: int) -> bool:
        current_year = datetime.now().year
        return isinstance(year, int) and 1950 <= year <= current_year
    
    @staticmethod
    def is_valid_length_km(length_km: float) -> bool:
        return isinstance(length_km, float) and length_km > 0
    
    @staticmethod
    def is_valid_number_of_laps(number_of_laps: int) -> bool:
        return isinstance(number_of_laps, int) and number_of_laps > 0
    
    @staticmethod
    def is_valid_fastest_lap_time(fastest_lap_time: Optional[float]) -> bool:
        if fastest_lap_time is None:
            return True
        return isinstance(fastest_lap_time, float) and fastest_lap_time > 0

class VerifyTeamUtils:

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return isinstance(name, str) and 0 < len(name) <= 100
    
    @staticmethod
    def is_valid_country(country: str) -> bool:
        return isinstance(country, str) and 0 < len(country) <= 100
    
    @staticmethod
    def is_valid_address(address: str) -> bool:
        return isinstance(address, str) and 0 < len(address) <= 100
    
    @staticmethod
    def is_valid_team_principal(team_principal: str) -> bool:
        return isinstance(team_principal, str) and 0 < len(team_principal) <= 100
    
    @staticmethod
    def is_valid_founded_year(founded_year: int) -> bool:
        current_year = datetime.now().year
        return isinstance(founded_year, int) and 1900 <= founded_year <= current_year
    
    @staticmethod
    def is_valid_total_points(total_points: float) -> bool:
        if isinstance(total_points, int):  # Allow integers too
            total_points = float(total_points)
        return isinstance(total_points, float) and total_points >= 0
    
    @staticmethod
    def is_valid_total_wins(total_wins: int) -> bool:
        return isinstance(total_wins, int) and total_wins >=0
    
    @staticmethod
    def is_valid_championships_won(championships_won: int) -> bool:
        return isinstance(championships_won, int) and championships_won >=0
    
    @staticmethod
    def is_valid_is_actual_champion(is_actual_champion: bool) -> bool:
        return isinstance(is_actual_champion, bool)

    @staticmethod
    def is_valid_logo_url(logo_url: Optional[str]) -> bool:
        if logo_url is None:
            return True
        return isinstance(logo_url, str) and len(logo_url) <= 255