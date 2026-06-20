from datetime import datetime

def calculate_age(birthdate_str, date_format="%Y-%m-%d"):
    birthdate = datetime.strptime(birthdate_str, date_format)
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
