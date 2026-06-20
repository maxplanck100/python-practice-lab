def validate_login(username, password, users_db):
    return users_db.get(username) == password
