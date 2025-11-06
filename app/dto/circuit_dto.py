from dataclasses import dataclass,field
from app.utils.verify_utils import VerifyCircuitUtils

from typing import Optional, Tuple, Dict

@dataclass
class CircuitCreateDTO:
    name: str
    city: str
    country: str
    first_grand_prix_year: int
    length_km: float
    number_of_laps: int
    fastest_lap_time: Optional[float] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['CircuitCreateDTO'], Optional[Dict]]:
        """
		Méthode statique qui sera apelée depuis le controlleur pour valider les données
		Elle retourne :
		- Un Tuple(DTO,None) si tout va bien
		- ou Elle retourne une erreur {"error": "Message"} Si un erreur est detectée
		"""

        if not data:
            return None, {"error": "No data provided"}
        
        # === Extracting Data | Normalization removing spaces ===

        name = (data.get('name') or "").strip()
        city = (data.get('city') or "").strip()
        country = (data.get('country') or "").strip()
        first_grand_prix_year = data.get('first_grand_prix_year')
        length_km = data.get('length_km')
        number_of_laps = data.get('number_of_laps')
        fastest_lap_time = data.get('fastest_lap_time') or None

        # === Required fields ===

        required_fields = {
            'name': name,
            'city': city,
            'country': country,
        }
        for field, value in required_fields.items():
            if value in [None, '']:
                return None, {"error": f"Missing field: {field}"}
        
        # === Validations ===

        if not VerifyCircuitUtils.is_valid_name(name):
            return None, {"error": "Invalid name"}
        
        if not VerifyCircuitUtils.is_valid_city(city):
            return None, {"error": "Invalid city"}
        
        if not VerifyCircuitUtils.is_valid_country(country):
            return None, {"error": "Invalid country"}
        
        if not VerifyCircuitUtils.is_valid_first_gp_year(first_grand_prix_year):
            return None, {"error": "Invalid first grand prix year"}
        
        if not VerifyCircuitUtils.is_valid_length_km(length_km):
            return None, {"error": "Invalid length in km"}
        
        if not VerifyCircuitUtils.is_valid_number_of_laps(number_of_laps):
            return None, {"error": "Invalid number of laps"}
        
        if not VerifyCircuitUtils.is_valid_fastest_lap_time(fastest_lap_time):
            return None, {"error": "Invalid fastest lap time"}
        
        return CircuitCreateDTO(
            name=name,
            city=city,
            country=country,
            first_grand_prix_year=first_grand_prix_year,
            length_km=length_km,
            number_of_laps=number_of_laps,
            fastest_lap_time=fastest_lap_time
        ), None
    
@dataclass
class CircuitUpdateDTO:
    name : str
    city : str
    country : str
    first_grand_prix_year : int
    length_km : float
    number_of_laps : int
    fastest_lap_time : Optional[float] = field(default=None)
    
    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['CircuitUpdateDTO'], Optional[Dict]]:
        if not data:
            return None, {"error": "Data missing for complete update"}
        
        dto, err = CircuitCreateDTO.from_json(data)

        if err:
            return None, err
        
        return CircuitUpdateDTO(
            name=dto.name,
            city=dto.city,
            country=dto.country,
            first_grand_prix_year=dto.first_grand_prix_year,
            length_km=dto.length_km,
            number_of_laps=dto.number_of_laps,
            fastest_lap_time=dto.fastest_lap_time
        ), None
        

@dataclass
class CircuitPatchDTO:
    name : Optional[str] = field(default=None)
    city : Optional[str] = field(default=None)
    country : Optional[str] = field(default=None)
    first_grand_prix_year : Optional[int] = field(default=None)
    length_km : Optional[float] = field(default=None)
    number_of_laps : Optional[int] = field(default=None)
    fastest_lap_time : Optional[float] = field(default=None)
    
    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['CircuitPatchDTO'], Optional[Dict]]:
        if not data:
            return None, {"error": "No data provided for patching"}

        name = data.get('name')
        city = data.get('city')
        country = data.get('country')
        first_grand_prix_year = data.get('first_grand_prix_year')
        length_km = data.get('length_km')
        number_of_laps = data.get('number_of_laps')
        fastest_lap_time = data.get('fastest_lap_time')

        # If no fields were provided at all, reject the patch
        if all(v is None for v in [name, city, country, first_grand_prix_year, length_km, number_of_laps, fastest_lap_time]):
            return None, {"error": "No fields provided for patch"}

        # Validate only the fields that are present
        if name is not None and not VerifyCircuitUtils.is_valid_name(name):
            return None, {"error": "Invalid name"}

        if city is not None and not VerifyCircuitUtils.is_valid_city(city):
            return None, {"error": "Invalid city"}

        if country is not None and not VerifyCircuitUtils.is_valid_country(country):
            return None, {"error": "Invalid country"}

        if first_grand_prix_year is not None and not VerifyCircuitUtils.is_valid_first_gp_year(first_grand_prix_year):
            return None, {"error": "Invalid first grand prix year"}

        if length_km is not None and not VerifyCircuitUtils.is_valid_length_km(length_km):
            return None, {"error": "Invalid length in km"}

        if number_of_laps is not None and not VerifyCircuitUtils.is_valid_number_of_laps(number_of_laps):
            return None, {"error": "Invalid number of laps"}

        if fastest_lap_time is not None and not VerifyCircuitUtils.is_valid_fastest_lap_time(fastest_lap_time):
            return None, {"error": "Invalid fastest lap time"}

        return CircuitPatchDTO(
            name=name,
            city=city,
            country=country,
            first_grand_prix_year=first_grand_prix_year,
            length_km=length_km,
            number_of_laps=number_of_laps,
            fastest_lap_time=fastest_lap_time
        ), None