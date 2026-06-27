password = input("Enter Password: ")

valid = True

if len(password) < 12:
    print("❌ Password should be at least 12 characters long")
    valid = False
else:
    print("✅ Minimum 12 characters")

if not any(char.isupper() for char in password):
    print("❌ Add at least one uppercase letter (A-Z)")
    valid = False
else:
    print("✅ Uppercase letter found")

if not any(char.islower() for char in password):
    print("❌ Add at least one lowercase letter (a-z)")
    valid = False
else:
    print("✅ Lowercase letter found")

if not any(char.isdigit() for char in password):
    print("❌ Add at least one number (0-9)")
    valid = False
else:
    print("✅ Number found")

if not any(char in "@#$%^&*!" for char in password):
    print("❌ Add at least one special character (@#$%^&*!)")
    valid = False
else:
    print("✅ Special character found")

print()

if valid:
    print("🟢 Strong Password")
else:
    print("🔴 Weak Password")
    password = input("Enter Password: ")

valid = True

if len(password) < 12:
    print("❌ Password should be at least 12 characters long")
    valid = False
else:
    print("✅ Minimum 12 characters")

if not any(char.isupper() for char in password):
    print("❌ Add at least one uppercase letter (A-Z)")
    valid = False
else:
    print("✅ Uppercase letter found")

if not any(char.islower() for char in password):
    print("❌ Add at least one lowercase letter (a-z)")
    valid = False
else:
    print("✅ Lowercase letter found")

if not any(char.isdigit() for char in password):
    print("❌ Add at least one number (0-9)")
    valid = False
else:
    print("✅ Number found")

if not any(char in "@#$%^&*!" for char in password):
    print("❌ Add at least one special character (@#$%^&*!)")
    valid = False
else:
    print("✅ Special character found")

print()

if valid:
    print("🟢 Strong Password")
else:
    print("🔴 Weak Password")
