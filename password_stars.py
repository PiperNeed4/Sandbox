minimum_length = 6
user_password = input("Enter password: ")
while len(user_password) < minimum_length:
    print("Password is too short")
    user_password = input("Enter password: ")
print("*" * len(user_password))
