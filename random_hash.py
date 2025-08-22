import random
import string
import hashlib
import sys

def generate_random_hash():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return hashlib.sha256(random_string.encode()).hexdigest()

def main(max_tries=1000):
    for i in range(max_tries):
        h = generate_random_hash()
        if h.startswith('00'):
            print(f"Hash empezando con '00': {h}")
            return 0  # success
    print("No se encontró ningún hash con dos ceros consecutivos al inicio.")
    return 1  # failure

if __name__ == "__main__":
    sys.exit(main())
