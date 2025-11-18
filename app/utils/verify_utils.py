import re
from typing import Optional
from datetime import date, datetime



# region Circuit
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
# endregion

# region Team
class VerifyTeamUtils:

    IMAGE_REGEX = re.compile(r"^.+\.(jpg|jpeg|png|gif|bmp|webp)$", re.IGNORECASE)

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
    def is_valid_logo_url(logo_url: str) -> bool:
        return bool(VerifyTeamUtils.IMAGE_REGEX.match(logo_url))
# endregion

# region Driver
class VerifyDriverUtils:

    IMAGE_REGEX = re.compile(r"^.+\.(jpg|jpeg|png|gif|bmp|webp)$", re.IGNORECASE)

    @staticmethod
    def is_valid_driver_ref(driver_ref: str) -> bool:
        return isinstance(driver_ref, str) and len(driver_ref) == 3
    
    @staticmethod
    def is_valid_first_name(first_name: str) -> bool:
        return isinstance(first_name, str) and 0 < len(first_name) <= 50
    
    @staticmethod
    def is_valid_last_name(last_name: str) -> bool:
        return isinstance(last_name, str) and 0 < len(last_name) <= 50
    
    @staticmethod
    def is_valid_nationality(nationality: str) -> bool:
        return isinstance(nationality, str) and 0 < len(nationality) <= 50
    
    @staticmethod
    def is_valid_birth_date(birth_date: Optional[str | date]) -> Optional[date]:
        if isinstance(birth_date, date):
            return birth_date
        if isinstance(birth_date, str):
            try:
                return datetime.strptime(birth_date, "%Y-%m-%d").date()
            except ValueError:
                return None
        return None
    
    @staticmethod
    def is_valid_is_actual_champion(is_actual_champion: bool) -> bool:
        return isinstance(is_actual_champion, bool)
    
    @staticmethod
    def is_valid_is_using_number_one(is_using_number_one: bool) -> bool:
        return isinstance(is_using_number_one, bool)
    
    @staticmethod
    def is_valid_car_number(car_number: int) -> bool:
        return isinstance(car_number, int) and car_number > 1
    
    @staticmethod
    def is_valid_total_points(total_points: float) -> bool:
        if isinstance(total_points, int):  # Allow integers too
            total_points = float(total_points)
        return isinstance(total_points, float) and total_points >= 0
    
    @staticmethod
    def is_valid_total_wins(total_wins: int) -> bool:
        return isinstance(total_wins, int) and total_wins >= 0
    
    @staticmethod
    def is_valid_total_podiums(total_podiums: int) -> bool:
        return isinstance(total_podiums, int) and total_podiums >= 0
    
    @staticmethod
    def is_valid_number_championship_won(number_championship_won: int) -> bool:
        return isinstance(number_championship_won, int) and number_championship_won >= 0
    
    @staticmethod
    def is_valid_image(image: str) -> bool:
        return bool(VerifyDriverUtils.IMAGE_REGEX.match(image))
    
    @staticmethod
    def is_valid_team_id(team_id: int) -> bool:
        return isinstance(team_id, int) and team_id >= 0
# endregion

# region Season
class VerifySeasonUtils:

    @staticmethod
    def is_valid_year(year: int) -> bool:
        current_year = datetime.now().year
        return isinstance(year, int) and 1900 <= year <= current_year
    
    @staticmethod
    def is_valid_is_current(is_current: bool) -> bool:
        return isinstance(is_current, bool)
    
    @staticmethod
    def is_valid_start_date(start_date: Optional[str | date]) -> Optional[date]:
        if isinstance(start_date, date):
            return start_date
        if isinstance(start_date, str):
            try:
                return datetime.strptime(start_date, "%Y-%m-%d").date()
            except ValueError:
                return None
        return None
    
    @staticmethod
    def is_valid_end_date(end_date: Optional[str | date]) -> Optional[date]:
        if isinstance(end_date, date):
            return end_date
        if isinstance(end_date, str):
            try:
                return datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return None
        return None
# endregion