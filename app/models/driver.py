from app.models import db

class Driver(db.Model):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True)
    driver_ref = db.Column(db.String(3), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    is_actual_champion = db.Column(db.Boolean, default=False)
    is_using_number_one = db.Column(db.Boolean, default=False)
    car_number = db.Column(db.Integer, nullable=False)
    total_points = db.Column(db.Float, default=0)
    total_wins = db.Column(db.Integer, default=0)
    total_podiums = db.Column(db.Integer, default=0)
    number_championship_won = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __repr__(self):
        return f'<Driver {self.first_name} has a total of {self.total_points} points.>'
    
    def to_dict(self):

        return {
            "id": self.id,
            "driver_ref": self.driver_ref,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "nationality": self.nationality,
            "birth_date": self.birth_date,
            "is_actual_champion": self.is_actual_champion,
            "is_using_number_one": self.is_using_number_one,
            "car_number": self.car_number,
            "total_points": self.total_points,
            "total_wins": self.total_wins,
            "total_podiums": self.total_podiums,
            "number_championships_won": self.number_championship_won,
            "image": self.image,
            "team_id": self.team_id
        }