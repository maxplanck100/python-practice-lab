import re

def is_palindrome(s):
    clean_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return clean_s == clean_s[::-1]
