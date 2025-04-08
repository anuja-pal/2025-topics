def categorize_by_age(age):
    if 0 <= age <=9:
        return "Child"
    elif age <= 18:
        return "Adolescent"
    elif age <= 65:
        return "Adult"
    elif age <= 150:
        return "Golden Age"
    else:
        return f"Invalid age: {age}"