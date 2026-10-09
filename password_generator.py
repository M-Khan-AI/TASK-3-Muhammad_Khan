import secrets
import string
import math

def get_length():
    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length >= 8:
                return length
            print("Too short. Use at least 8 characters.")
        except ValueError:
            print("Please enter a whole number.")

def generate_password(length, use_symbols=False):
    pool = string.ascii_letters + string.digits
    if use_symbols:
        pool += string.punctuation
    return ''.join(secrets.choice(pool) for _ in range(length))

def entropy_bits(length, pool_size):
    return length * math.log2(pool_size)

if __name__ == "__main__":
    length = get_length()
    symbols = input("Include symbols? (y/n): ").lower() == "y"
    pwd = generate_password(length, symbols)
    pool_size = 62 + (len(string.punctuation) if symbols else 0)
    print(f"Password: {pwd}")
    print(f"Entropy: {entropy_bits(length, pool_size):.1f} bits")