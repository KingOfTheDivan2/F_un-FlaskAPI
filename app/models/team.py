from app.models import db

class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    team_principal = db.Column(db.String(100), nullable=False)
    founded_year = db.Column(db.Integer, nullable=False)
    total_points = db.Column(db.Float, default=0)
    total_wins = db.Column(db.Integer, default=0)
    championships_won = db.Column(db.Integer, default=0)
    is_actual_champion = db.Column(db.Boolean, default=False)
    logo_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Team {self.name} based in {self.base}>'
    
    def to_dict(self):
        """Return a JSON-serializable representation of the Team."""
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "address": self.address,
            "team_principal": self.team_principal,
            "founded_year": self.founded_year,
            "total_points": self.total_points,
            "total_wins": self.total_wins,
            "championships_won": self.championships_won,
            "is_actual_champion": self.is_actual_champion,
            "logo_url": self.logo_url
        }