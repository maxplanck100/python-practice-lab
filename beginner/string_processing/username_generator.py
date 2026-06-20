def generate_username(first_name, last_name, year):
    return f"{first_name[0].lower()}{last_name.lower()}{str(year)[-2:]}"
