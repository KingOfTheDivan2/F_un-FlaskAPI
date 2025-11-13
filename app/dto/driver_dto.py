from dataclasses import dataclass, field
from app.utils.verify_utils import VerifyDriverUtils
from datetime import date, datetime

from typing import Optional, Tuple, Dict

@dataclass
class DriverCreateDTO:
    driver_ref: str
    first_name: str
    last_name: str
    nationality: str
    birth_date: date
    is_actual_champion: bool
    is_using_number_one: bool
    car_number: int
    team_id: int
    total_points: Optional[float] = field(default=0)
    total_wins: Optional[int] = field(default=0)
    total_podiums: Optional[int] = field(default=0)
    number_championship_won: Optional[int] = field(default=0)
    image: Optional[str] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['DriverCreateDTO'], Optional[Dict]]:

        if not data:
            return None, {"error": "No data provided"}
        
        # === Extracting data | Normalization removing spaces ===

        driver_ref = (data.get('driver_ref') or "").strip().upper()
        first_name = (data.get('first_name') or "").strip().capitalize()
        last_name = (data.get('last_name') or "").strip().capitalize()
        nationality = (data.get('nationality') or "").strip().capitalize()
        birth_date = (data.get('birth_date'))
        is_actual_champion = data.get('is_actual_champion')
        if is_actual_champion == True:
            is_using_number_one = data.get('is_using_number_one')
        else:
            is_using_number_one = False
        car_number = data.get('car_number')
        team_id = data.get('team_id')
        total_points = data.get('total_points', 0)
        total_wins = data.get('total_wins', 0)
        total_podiums = data.get('total_podiums', 0)
        number_championship_won = data.get('number_championship_won', 0)
        image = (data.get('image') or "").strip() or None

        # === Check the date format ===

        if isinstance(birth_date, str):
            try:
                birthdate_obj = datetime.strptime(birth_date, "%Y-%m-%d").date()
            except ValueError:
                return None, {"error": "birthdate must be in format YYYY-MM-DD"}
        elif isinstance(birth_date, date):
            birthdate_obj = birth_date
        else:
            return None, {"error": "birthdate must be a string or date"}
        
        # === Required fields ===

        required_fields = {
            'driver_ref': driver_ref,
            'first_name': first_name,
            'last_name': last_name,
            'nationality': nationality,
            'birth_date': birth_date,
            'is_actual_champion': is_actual_champion,
            'is_using_number_one': is_using_number_one,
            'car_number': car_number,
            'team_id': team_id
        }
        for field, value in required_fields.items():
            if value in [None, '']:
                return None, {"error": f"Missing field: {field}"}
        
        # === Validations ===

        if not VerifyDriverUtils.is_valid_driver_ref(driver_ref):
            return None, {"error": "Invalid driver ref"}
        
        if not VerifyDriverUtils.is_valid_first_name(first_name):
            return None, {"error": "Invalid first name"}
        
        if not VerifyDriverUtils.is_valid_last_name(last_name):
            return None, {"error": "Invalid last name"}
        
        if not VerifyDriverUtils.is_valid_nationality(nationality):
            return None, {"error": "Invalid nationality"}
        
        if not VerifyDriverUtils.is_valid_birth_date(birth_date):
            return None, {"error": "Invalid birth date"}
        
        if not VerifyDriverUtils.is_valid_is_actual_champion(is_actual_champion):
            return None, {"error": "Invalid is actual champion"}
        
        if not VerifyDriverUtils.is_valid_is_using_number_one(is_using_number_one):
            return None, {"error": "Invalid is using number one"}
        
        if not VerifyDriverUtils.is_valid_car_number(car_number):
            return None, {"error": "Invalid car number"}
        
        if not VerifyDriverUtils.is_valid_team_id(team_id):
            return None, {"error": "Invalid team id"}
        
        if not VerifyDriverUtils.is_valid_total_points(total_points):
            return None, {"error": "Invalid total points"}
        
        if not VerifyDriverUtils.is_valid_total_wins(total_wins):
            return None, {"error": "Invalid total wins"}
        
        if not VerifyDriverUtils.is_valid_total_podiums(total_podiums):
            return None, {"error": "Invalid total podiums"}
        
        if not VerifyDriverUtils.is_valid_number_championship_won(number_championship_won):
            return None, {"error": "Invalid number of championships won"}
        
        if not VerifyDriverUtils.is_valid_image(image):
            return None, {"error": "Invalid image"}
        
        return DriverCreateDTO(
            driver_ref=driver_ref,
            first_name=first_name,
            last_name=last_name,
            nationality=nationality,
            birth_date=birthdate_obj,
            is_actual_champion=is_actual_champion,
            is_using_number_one=is_using_number_one,
            car_number=car_number,
            team_id=team_id,
            total_points=total_points,
            total_wins=total_wins,
            total_podiums=total_podiums,
            number_championship_won=number_championship_won,
            image=image
        ), None

@dataclass
class DriverUpdateDTO:
    driver_ref: str
    first_name: str
    last_name: str
    nationality: str
    birth_date: date
    is_actual_champion: bool
    is_using_number_one: bool
    car_number: int
    team_id: int
    total_points: Optional[float] = field(default=0)
    total_wins: Optional[int] = field(default=0)
    total_podiums: Optional[int] = field(default=0)
    number_championship_won: Optional[int] = field(default=0)
    image: Optional[str] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['DriverUpdateDTO'], Optional[Dict]]:

        if not data:
            return None, {"error": "Data missing for complete update"}
        
        dto, err = DriverCreateDTO.from_json(data)

        if err:
            return None, err
        
        try:
            # Conversion explicite de la date si nécessaire
            birthdate_str = data.get("birth_date")
            birthdate_obj = (
                datetime.strptime(birthdate_str, "%Y-%m-%d").date()
                if isinstance(birthdate_str, str)
                else birthdate_str
            )
        
            return DriverUpdateDTO(
                driver_ref=dto.driver_ref,
                first_name=dto.first_name,
                last_name=dto.last_name,
                nationality=dto.nationality,
                birth_date=birthdate_obj,
                is_actual_champion=dto.is_actual_champion,
                is_using_number_one=dto.is_using_number_one,
                car_number=dto.car_number,
                team_id=dto.team_id,
                total_points=dto.total_points,
                total_wins=dto.total_wins,
                total_podiums=dto.total_podiums,
                number_championship_won=dto.number_championship_won,
                image=dto.image
            ), None
        except KeyError as e:
            return None, {"error": f"Missing field: {str(e)}"}
        except ValueError as e:
            return None, {"error": f"Invalid value: {str(e)}"}

@dataclass
class DriverPatchDTO:
    driver_ref: Optional[str] = field(default=None)
    first_name: Optional[str] = field(default=None)
    last_name: Optional[str] = field(default=None)
    nationality: Optional[str] = field(default=None)
    birth_date: Optional[date] = field(default=None)
    is_actual_champion: Optional[bool] = field(default=None)
    is_using_number_one: Optional[bool] = field(default=None)
    car_number: Optional[int] = field(default=None)
    team_id: Optional[int] = field(default=None)
    total_points: Optional[float] = field(default=None)
    total_wins: Optional[int] = field(default=None)
    total_podiums: Optional[int] = field(default=None)
    number_championship_won: Optional[int] = field(default=None)
    image: Optional[str] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['DriverPatchDTO'], Optional[Dict]]:
        if not data:
            return None, {"error": "No data provided for patching"}
        
        errors = {}

        def normalize(field, transform=lambda x: x.strip()):
            return transform(data.get(field) or "").strip() or None

        driver_ref = normalize("sriver_ref", lambda x: x.strip().upper())
        first_name = normalize("first_name", lambda x: x.strip().capitalize())
        last_name = normalize("last_name", lambda x: x.strip().capitalize())
        nationality = normalize("nationality", lambda x: x.strip().capitalize())
        birth_date = data.get('birth_date')
        is_actual_champion = data.get('is_actual_champion')
        if is_actual_champion == True:
            is_using_number_one = data.get('is_using_number_one')
        else:
            is_using_number_one = False
        car_number = data.get('car_number')
        team_id = data.get('team_id')
        total_points = data.get('total_points')
        total_wins = data.get('total_wins')
        total_podiums = data.get('total_podiums')
        number_championship_won = data.get('number_championship_won')
        image = data.get('image')

        birthdate_obj = None
        if birth_date:
            if isinstance(birth_date, str):
                try:
                    birthdate_obj = datetime.strptime(birth_date, "%Y-%m-%d").date()
                except ValueError:
                    errors["birth_date"] = "birth date must be in format YYYY-MM-DD"
            elif isinstance(birth_date, date):
                birthdate_obj = birth_date
            else:
                errors["birth_date"] = "birth date must be a string or date"

        if errors:
            return None, errors
        
        if all(v is None for v in [driver_ref, first_name, last_name, nationality, birth_date, is_actual_champion, is_using_number_one, car_number, team_id, total_points, total_wins,total_podiums, number_championship_won, image]):
            return None, {"error": "No fields provided for patch"}
        
        if driver_ref is not None and not VerifyDriverUtils.is_valid_driver_ref(driver_ref):
            return None, {"error": "Invalid driver ref"}
        
        if first_name is not None and not VerifyDriverUtils.is_valid_first_name(first_name):
            return None, {"error": "Invalid first name"}
        
        if last_name is not None and not VerifyDriverUtils.is_valid_last_name(last_name):
            return None, {"error": "Invalid last name"}
        
        if nationality is not None and not VerifyDriverUtils.is_valid_nationality(nationality):
            return None, {"error": "Invalid nationality"}
        
        if birth_date is not None and not VerifyDriverUtils.is_valid_birth_date(birth_date):
            return None, {"error": "Invalid birth date"}
        
        if is_actual_champion is not None and not VerifyDriverUtils.is_valid_is_actual_champion(is_actual_champion):
            return None, {"error": "Invalid is actual champion"}
        
        if is_using_number_one is not None and not VerifyDriverUtils.is_valid_is_using_number_one(is_using_number_one):
            return None, {"error": "Invalid is using number one"}
        
        if car_number is not None and not VerifyDriverUtils.is_valid_car_number(car_number):
            return None, {"error": "Invalid car number"}
        
        if team_id is not None and not VerifyDriverUtils.is_valid_team_id(team_id):
            return None, {"error": "Invalid team id"}
        
        if total_points is not None and not VerifyDriverUtils.is_valid_total_points(total_points):
            return None, {"error": "Invalid total points"}
        
        if total_wins is not None and not VerifyDriverUtils.is_valid_total_wins(total_wins):
            return None, {"error": "Invalid total wins"}
        
        if total_podiums is not None and not VerifyDriverUtils.is_valid_total_podiums(total_podiums):
            return None, {"error": "Invalid total podiums"}
        
        if number_championship_won is not None and not VerifyDriverUtils.is_valid_number_championship_won(number_championship_won):
            return None, {"error": "Invalid number of championships won"}
        
        if image is not None and not VerifyDriverUtils.is_valid_image(image):
            return None, {"error": "Invalid image"}
        
        return DriverPatchDTO(
            driver_ref=driver_ref,
            first_name=first_name,
            last_name=last_name,
            nationality=nationality,
            birth_date=birthdate_obj,
            is_actual_champion=is_actual_champion,
            is_using_number_one=is_using_number_one,
            car_number=car_number,
            team_id=team_id,
            total_points=total_points,
            total_wins=total_wins,
            total_podiums=total_podiums,
            number_championship_won=number_championship_won,
            image=image
        ), None