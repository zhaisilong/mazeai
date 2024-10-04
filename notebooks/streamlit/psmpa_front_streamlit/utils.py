def write_tmp(content: str, fname: str = 'tmp.txt') -> None:
    with open(fname, 'a') as f:
        f.write(content)

def resource_is_available():
    return True

def is_sequence_file_valid(file):
    # if file is not None:
    #     bytes_data = file.getvalue()
    return True

def is_feature_file_valid(file):
    return True

def send_mail(email, result):
    try:
        return 'Success'
    except:
        return None