def validate_password(password):
    errors = []
    if not (6 <= len(password) <= 10):
        errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")
    
    digits_count = sum(1 for char in password if char.isdigit())
    if digits_count < 2:
        errors.append("Password must have at least 2 digits")
    
    return errors

pwd = input()
validation_errors = validate_password(pwd)
if not validation_errors:
    print("Password is valid")
else:
    for err in validation_errors:
        print(err)
