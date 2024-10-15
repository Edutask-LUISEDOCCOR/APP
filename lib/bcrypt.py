import bcrypt

def hash_password (password):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hash

def verify_password (inputPassword, password):
    return bcrypt.checkpw(inputPassword.encode("utf-8"), password.encode("utf-8"))