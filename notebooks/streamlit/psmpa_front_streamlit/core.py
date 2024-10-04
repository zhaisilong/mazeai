import time
import os

def run_anylisis(sname, fname):
    try:
        result_name = sname + fname + '.result'
        result_path = os.path.join('result', result_name)
        time.sleep(5)
        return result_path
    except:
        return None