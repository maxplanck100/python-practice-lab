def extract_extension(filename):
    if '.' in filename:
        return filename.rsplit('.', 1)[-1]
    return ''
