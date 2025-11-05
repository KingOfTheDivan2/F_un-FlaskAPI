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