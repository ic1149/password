import argon2
import os

password = "mysecretpassword"

ph = argon2.PasswordHasher(time_cost=3, memory_cost=65536,
                           parallelism=4, hash_len=32, salt_len=16,
                           encoding='utf-8')

password_hashed = ph.hash(password.encode('utf-8'))
print(password_hashed)
try:
    ph.verify(password_hashed,"mysecretpassword")
except argon2.exceptions.VerifyMismatchError:
    print("wrong password")
else:
    print("correct password")
