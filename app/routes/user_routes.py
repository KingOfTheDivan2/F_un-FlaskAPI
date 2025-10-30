from flask import Blueprint, request, jsonify
from app.controllers.user_controllers import (
    create_user,
    authenticate_user,
    get_user_by_id,
    update_user,
    update_password,
    delete_user,
    get_all_users,
    change_user_role
)

from app.utils.jwt_utils import jwt_required, admin_required,generate_token

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/', methods=['POST'])
def register_user():
    # recupere les donnees du corps de la requete
    data = request.get_json()
    # Creation de l'utilisateur
    user = create_user(data)
    
    # Verification de la creation
    if not user:
        return jsonify({'message': 'User creation failed'}), 400
    elif user:
        # Generation du token JWT
        token = generate_token(user.id,user.role)
        # Retourne le token dans la reponse avec les informations désirées
        return jsonify({
            'username' : user.username,
            'token': token,
        }),201

@user_bp.route('/login', methods=['POST'])
def login_user():
    # recuperation des donnees du corps de la requete
    data = request.get_json()
    
    user = authenticate_user(data['email'], data['password'])
    
    # Si l'authentification echoue on renvoie une erreur 401
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = generate_token(user.id,user.role)
    return jsonify({
        'username' : user.username,
        'token': token,
    }), 200
    
@user_bp.route('/details', methods=['GET'])
# Route protégée par le token
@jwt_required
def get_user(user_id,role):
    # Recuperation de l'utilisateur par son id
    user = get_user_by_id(user_id)
    
    # Si l'utilisateur n'existe pas on renvoie une erreur 404
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    # On renvoie les informations souhaité de l'utilisateur
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    })
    
@user_bp.route('/update', methods=['PUT'])
# Route protégée par le token
@jwt_required
def update_user_info(user_id,role):
    # recupere les donnees du corps de la requete
    data = request.get_json()
    
    # Mise a jour de l'utilisateur
    user = update_user(user_id, data)
    
    # Si la reponse ne correspond pas on renvoie une erreur
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    # On renvoir un message de succes
    return jsonify({'message': 'User updated successfully'}), 200


@user_bp.route('/password', methods=['PUT'])
# Route protégée par le token
@jwt_required
# l'id est fournie par le token
def update_user_password(user_id,role):
    # On recupere les donnees du corps de la requete
    data = request.get_json()
    
    result = update_password(user_id, data['old_password'], data['new_password'])
    
    if not result:
        return jsonify({'message': 'Password update failed'}), 400
    
    return jsonify({
        'message': 'Password updated successfully',
    }), 200
    

@user_bp.route('/<int:user_id_to_delete>', methods=['DELETE'])
@jwt_required
def delete_user_account(user_id_to_delete,user_id,role):
    
    # Suppression de l'utilisateur
    response = delete_user(user_id_to_delete,role)
    
    if not response:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify({'message': 'User deleted successfully'}), 200

# Admin 

# Recuperation de tous les utilisateurs
@user_bp.route('/', methods=['GET'])
@admin_required
def get_all_users_route():
    users = get_all_users()
    return jsonify(
        [{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    }for user in users]
        ), 200
    

@user_bp.route('adminrole/<int:user_id_to_update>', methods=['PUT'])
@admin_required
def update_role_user(user_id_to_update):
    # recupere les donnees du corps de la requete
    data = request.get_json()
    
    if 'role' not in data:
        return jsonify({'message': 'Role is required'}), 400
    
    new_role = data['role']
    
    result = change_user_role(user_id_to_update, new_role)
    
    if not result:
        return jsonify({'message': 'Role update failed'}), 400
    
    return jsonify({'message': 'User role updated successfully'}), 200