def check_age(age):
    if age < 18:
        print("You are a minor.")
    elif 18 <= age < 65:
        return("You are an adult.")
    else:
        print("You are a senior citizen.")


check_age(15)  # Output: You are a minor.
check_age(11)  # Output: You are an adult.
check_age(33)  # Output: You are an adult.