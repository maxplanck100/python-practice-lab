import random

def rock_paper_scissors(player_move):
    moves = ["Rock", "Paper", "Scissors"]
    computer_move = random.choice(moves)
    if player_move == computer_move:
        return f"Tie ({computer_move})"
    win_conditions = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    if win_conditions.get(player_move) == computer_move:
        return f"Win ({computer_move})"
    return f"Lose ({computer_move})"
