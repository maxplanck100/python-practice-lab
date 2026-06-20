import os
import shutil

def file_organizer(directory):
    if not os.path.exists(directory):
        return
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            ext = filename.split('.')[-1] if '.' in filename else 'misc'
            ext_dir = os.path.join(directory, ext)
            os.makedirs(ext_dir, exist_ok=True)
            shutil.move(filepath, os.path.join(ext_dir, filename))
