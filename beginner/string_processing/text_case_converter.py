def convert_case(text, case_type="lower"):
    if case_type == "lower":
        return text.lower()
    if case_type == "upper":
        return text.upper()
    if case_type == "title":
        return text.title()
    return text
