import os
import sys
import shutil
from time import localtime, strftime

class logging_service(object):

    def __init__(self):
        base_path = os.path.abspath(__file__)
        base_dir = base_path[0 : base_path.rfind("/") + 1]
        self.log_dir = base_dir + "logs/"
        log_file_time = strftime("%Y-%m-%d---%H:%M:%S", localtime())
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.log_data_file = self.log_dir + log_file_time + ".log"
        self.file = open(self.log_data_file, "w+")

    def write_data(self, data):
        current_time = strftime("%Y-%m-%d---%H:%M:%S:\t", localtime())
        line = current_time + data
        self.file.write(line)

    def close_log(self):
        self.file.close()

    def clear_all_logs(self):
        self.close_log()
        shutil.rmtree(self.log_dir)
