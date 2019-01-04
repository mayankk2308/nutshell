import os
import sys
import shutil
from time import localtime, strftime
from directory_service import LOG_DIR

class log_service(object):

    def __init__(self):
        log_file_time = strftime("%Y-%m-%d---%H:%M:%S", localtime())
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        self.log_data_file = LOG_DIR + log_file_time + ".log"
        self.file = open(self.log_data_file, "w+")

    def write_data(self, data):
        current_time = strftime("%Y-%m-%d---%H:%M:%S:\t", localtime())
        line = current_time + data
        self.file.write(line + "\n")

    def close_log(self):
        self.file.close()

    def clear_all_logs(self):
        self.close_log()
        shutil.rmtree(LOG_DIR)
