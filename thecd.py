# project: CLI Password Strength Checker.

def password_checker():

    password = input("Enter your password: ")

    checklist = {
    "length": len(password) >= 12,
    "uppercase": any(char.isupper() for char in password),
    "lowercase": any(char.islower()for char in password),
    "digit": any(char.isdigit()for char in password),
    "special": any(not char.isalnum() for char in password),
}
    if all(checklist.values()):
        print("Your password is strong.")
    else:
        print("Your password is strong or moderate")

        for key, passed in checklist.items():
            if not passed:
                print(f" your password is missing: {key}, hence making it weak.")

password_checker()

