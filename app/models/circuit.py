from app.models import db


class Circuit(db.Model):
    __tablename__ = 'circuit'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    city = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    first_grand_prix_year = db.Column(db.Integer, nullable=False)
    length_km = db.Column(db.Float, nullable=False)
    number_of_laps = db.Column(db.Integer, nullable=False)
    fastest_lap_time = db.Column(db.Float, nullable=True)  # in seconds
    
    def __repr__(self):
        return f'<Circuit {self.name} located in {self.city}, {self.country}>'
    
    def to_dict(self):
        """Return a JSON-serializable representation of the Circuit."""
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "country": self.country,
            "first_grand_prix_year": self.first_grand_prix_year,
            "length_km": self.length_km,
            "number_of_laps": self.number_of_laps,
            "fastest_lap_time": self.fastest_lap_time
}