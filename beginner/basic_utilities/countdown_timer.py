import time

def countdown_timer(seconds):
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
