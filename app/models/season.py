from app.models import db

class Season(db.Model):
    __tablename__ = 'season'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    is_current = db.Column(db.Boolean, default=False)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Season {self.year} has started on {self.start_date}.>'
    
    def to_dict(self):

        return {
            "id": self.id,
            "year": self.year,
            "is_current": self.is_current,
            "start_date": self.start_date,
            "end_date": self.end_date
        }