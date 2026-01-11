
# Password strength checker using flags

password = input("Enter password: ")

has_letter = False
has_digit = False

for ch in password:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_digit = True

    if has_letter and has_digit:
        break

if has_letter and has_digit:
    print("Strong password")
else:
    print("Weak password")
