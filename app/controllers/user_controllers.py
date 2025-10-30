from sqlalchemy import true
from app.models import db,User
from werkzeug.security import generate_password_hash, check_password_hash



# Creation d'un utilisateur
def create_user(data):
    hashed_password = generate_password_hash(data['password'])
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )
    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    
    return new_user

# Authentification d'un utilisateur
def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

# Recuperation par id
def get_user_by_id(user_id):
    return User.query.get(user_id)

# update d'un utilisateur
def update_user(user_id, data):
    user = User.query.get(user_id)
    
    if not user:
        return None
    
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    
    db.session.commit()
    return user

# update password d'un utilisateur
def update_password(user_id, old_password, new_password):
    user = User.query.get(user_id)
    
    if not user:
        return None
    

    if not check_password_hash(user.password, old_password):
        return None
    
    try:
        user.password = generate_password_hash(new_password)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return { "error": f'Database error {str(e)}' }

# Suppression d'un utilisateur
def delete_user(user_id_to_delete,role):
    user = User.query.get(user_id_to_delete)
    
    if user.id != user_id_to_delete:
        if role == 'admin':
            db.session.delete(user)
            
    else:
        db.session.delete(user)
    
    if not user:
        return None
    
    db.session.delete(user)
    db.session.commit()
    return user

# Admin
# Recuperation de tous les utilisateurs
def get_all_users():
    return User.query.all()

# Admin
# Modifier le role d'un utilisateur
def change_user_role(user_id, new_role):
    # Definir les roles autorisés
    valid_roles = ['user', 'admin']
    
    if new_role not in valid_roles:
        return { "error": 'Invalid role' }
    
    user = User.query.get(user_id)
    if not user:
        return None
    
    try:
        user.role = new_role
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        return { "error": f'Database error {str(e)}' }
    