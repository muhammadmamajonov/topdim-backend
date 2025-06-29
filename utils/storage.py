import os
import uuid


def save_file(folder, file, request=None):
    
    filename = uuid.uuid4()
    extention = file.filename.split(".")[-1]
    file_path = f"./media/{folder}/{filename}.{extention}"
    
    with open(file_path, 'wb') as ph:
        ph.write(file.file.read())
    
    return file_path[2:]


def delete_file(file):

    if os.path.isfile(file):
        os.remove(file)