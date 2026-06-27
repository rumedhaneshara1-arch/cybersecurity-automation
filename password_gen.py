# Secure Password Generator Engine
# Built by Arch-Rumedha for ANC Cybersecurity Tracks

import random
import string

def generate_secure_key():
    print("====================================")
    print("🔐    SILICON SECURITY KEY v1.0     ")
    print("====================================")
    
    # Define the cryptographic characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Set password length to a secure 16-character block
    password_length = 16
    
    # Generate the random secure string
    secure_password = "".join(random.choice(all_chars) for i in range(password_length))
    
    print("\n▶ [SUCCESS] New Cryptographic Key Generated:")
    print("👉 " + secure_password)
    print("====================================")

# Execute the security engine
generate_secure_key()
