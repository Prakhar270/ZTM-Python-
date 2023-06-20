import re

pattern = re.compile(r"[a-zA-Z0-9@#$%]{8,}\d")

passw = input("Enter password: ")

checker = re.fullmatch(pattern, passw)

print(f"your password is correct") if checker is not None else print("Opps password requirements doesn't match")
