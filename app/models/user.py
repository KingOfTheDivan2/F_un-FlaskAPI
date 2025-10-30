from flask_login import UserMixin
from app.models import db

# Flask Login gere la connection /deconnection des utilisateurs
# UserMixin fournit des implémentations par défaut pour les méthodes requises par Flask-Login
class User(db.Model , UserMixin):
    __tablename__= 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)
    role = db.Column(db.String(20),nullable=False,default='user')  # Rôle par défaut 'user'
    
    # todos  : le nom du model auquel on fait reference
    # Backref permet d'accéder aux todos d'un utilisateur via user.todos
    # lazy=True charge les todos uniquement lorsque l'attribut est accédé
    # todos = db.relationship('Todo', backref='user', lazy=True)