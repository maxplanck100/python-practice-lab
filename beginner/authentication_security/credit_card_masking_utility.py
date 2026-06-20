import re

def mask_credit_card(card_number):
    card_number = re.sub(r'\D', '', str(card_number))
    if len(card_number) < 4:
        return card_number
    return '*' * (len(card_number) - 4) + card_number[-4:]
