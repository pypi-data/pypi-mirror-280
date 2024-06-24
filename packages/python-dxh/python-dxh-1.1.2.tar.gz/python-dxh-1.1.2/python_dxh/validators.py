def strong_password(password):
    return any(c.isupper() for c in password) and \
        any(c.islower() for c in password) and \
        any(c.isdigit() for c in password) and \
        any(c in '!@#$%^&*()-_=+[]{};:,.<>?/|' for c in password)
