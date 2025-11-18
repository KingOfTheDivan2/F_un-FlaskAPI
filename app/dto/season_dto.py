from dataclasses import dataclass, field
from app.utils.verify_utils import VerifySeasonUtils
from datetime import date, datetime

from typing import Optional, Tuple, Dict

@dataclass
class SeasonCreateDTO:
    year: int
    is_current: bool
    start_date: Optional[date] = field(default=None)
    end_date: Optional[date] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['SeasonCreateDTO'], Optional[Dict]]:

        if not data:
            return None, {"error": "No data provided"}
        
        # === Extracting data | Normalization removing spaces ===

        year = data.get('year')
        is_current = data.get('is_current')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # === Check the date format ===

        if isinstance(start_date, str):
            try:
                start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            except ValueError:
                return None, {"error": "start date must be in format YYYY-MM-DD"}
        elif isinstance(start_date, date):
            start_date_obj = start_date
        else:
            return None, {"error": "start date must be a string or date"}

        if isinstance(end_date, str):
            try:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return None, {"error": "end date must be in format YYYY-MM-DD"}
        elif isinstance(end_date, date):
            end_date_obj = end_date
        else:
            return None, {"error": "end date must be a string or date"}
        
        # === Required fields ===

        required_fields = {
            'year': year,
            'is_current': is_current,
            'start_date': start_date
        }
        for field, value in required_fields.items():
            if value in {None, ''}:
                return None, {"error": f"Missing field: {field}"}
        
        # === Validations ===

        if not VerifySeasonUtils.is_valid_year(year):
            return None, {"error": "Invalid year"}
        
        if not VerifySeasonUtils.is_valid_is_current(is_current):
            return None, {"error": "Invaid is current"}
        
        if not VerifySeasonUtils.is_valid_start_date(start_date):
            return None, {"error": "Invalid start date"}
        
        if not VerifySeasonUtils.is_valid_end_date(end_date):
            return None, {"error": "Invalid end date"}
        
        return SeasonCreateDTO(
            year=year,
            is_current=is_current,
            start_date=start_date_obj,
            end_date=end_date_obj
        ), None

@dataclass
class SeasonUpdateDTO:
    year: int
    is_current: bool
    start_date: Optional[date] = field(default=None)
    end_date: Optional[date] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['SeasonUpdateDTO'], Optional[Dict]]:

        if not data:
            return None, {"error": "Data missing for complete update"}
        
        dto, err = SeasonCreateDTO.from_json(data)

        if err:
            return None, err
        
        try:
            # Conversion explicite de la date si nécessaire
            start_date_str = data.get("start_date")
            start_date_obj = (
                datetime.strptime(start_date_str, "%Y-%m-%d").date()
                if isinstance(start_date_str, str)
                else start_date_str
            )

            end_date_str = data.get("end_date")
            end_date_obj = (
                datetime.strptime(end_date_str, "%Y-%m-%d").date()
                if isinstance(end_date_str, str)
                else end_date_str
            )

            return SeasonUpdateDTO(
                year=dto.year,
                is_current=dto.is_current,
                start_date=dto.start_date,
                end_date=dto.end_date
            ), None
        except KeyError as e:
            return None, {"error": f"Missing field: {str(e)}"}
        except ValueError as e:
            return None, {"error": f"Invalid Value: {str(e)}"}

@dataclass
class SeasonPatchDTO:
    year: Optional[int] = field(default=None)
    is_current: Optional[bool] = field(default=None)
    start_date: Optional[date] = field(default=None)
    end_date: Optional[date] = field(default=None)

    @staticmethod
    def from_json(data: dict) -> Tuple[Optional['SeasonPatchDTO'], Optional[Dict]]:
        if not data:
            return None, {"error": "No data provided for patching"}
        
        errors = {}

        year = data.get('year')
        is_current = data.get('is_current')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        start_date_obj = None
        if start_date:
            if isinstance(start_date, str):
                try:
                    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
                except ValueError:
                    errors["start_date"] = "start date must be in format YYYY-MM-DD"
            elif isinstance(start_date, date):
                start_date_obj = start_date
            else:
                errors["start_date"] = "start date must be a string or date"
            
        end_date_obj = None
        if end_date:
            if isinstance(end_date, str):
                try:
                    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
                except ValueError:
                    errors["end_date"] = "end date must be in format YYYY-MM-DD"
            elif isinstance(end_date, date):
                end_date_obj = end_date
            else:
                errors["end_date"] = "end date must be a string or date"

        if errors:
            return None, errors
        
        if all(v is None for v in [year, is_current, start_date, end_date]):
            return None, {"error": "No fields provided for patch"}
        
        if year is not None and not VerifySeasonUtils.is_valid_year(year):
            return None, {"error": "Invalid year"}
        
        if is_current is not None and not VerifySeasonUtils.is_valid_is_current(is_current):
            return None, {"error": "Invalid is_current"}
        
        if start_date is not None and not VerifySeasonUtils.is_valid_start_date(start_date):
            return None, {"error": "Invalid start date"}
        
        if end_date is not None and not VerifySeasonUtils.is_valid_end_date(end_date):
            return None, {"error": "Invalid end date"}
        
        return SeasonPatchDTO(
            year=year,
            is_current=is_current,
            start_date=start_date,
            end_date=end_date
        ), None