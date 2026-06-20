def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    if from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    return value
