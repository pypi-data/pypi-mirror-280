import os, time
def wait_until_file_exists(file_path, sleep_interval):
    while not os.path.exists(file_path):
        time.sleep(sleep_interval)
    return True