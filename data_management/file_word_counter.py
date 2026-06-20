def file_word_counter(filepath):
    try:
        with open(filepath, 'r') as file:
            return len(file.read().split())
    except FileNotFoundError:
        return 0
