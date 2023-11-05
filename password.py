import string
import secrets

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Example usage: Generate a password of length 16
password = generate_password(16)
print("Generated Password:", password)
