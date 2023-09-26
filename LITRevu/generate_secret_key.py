import random

def get_random_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join(random.SystemRandom().choice(chars) for i in range(50))

if __name__ == "__main__":
    print(get_random_secret_key())
