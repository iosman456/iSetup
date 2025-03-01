import itertools
import string

def brute_force_crack(password, max_length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return f"Password cracked: {guess} in {attempts} attempts"
    return "Password not found"

# Example usage
password = input("Enter the password to crack: ")
result = brute_force_crack(password)
print(result)