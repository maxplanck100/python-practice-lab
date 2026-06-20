def number_guessing_game(guess, target):
    if guess < target: return "Too low"
    if guess > target: return "Too high"
    return "Correct"
