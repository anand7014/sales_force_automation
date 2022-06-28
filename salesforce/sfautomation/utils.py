import os
def check_upload_file_size(attached_file):
    if os.stat(attached_file).st_size > 1000000:
        raise FileExistsError
    