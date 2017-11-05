import subprocess
import os

class script_manager(object):

    # parse command and extract expected arguments
    def parse_command(self, command, expected_args):
        quotes = 0
        command += " "
        current_arg = ""
        arg_count = -1
        args = []
        for character in command:
            if character is " " and quotes % 2 == 0:
                arg_count += 1
                args.append(current_arg)
                current_arg = ""
            elif character is "'":
                quotes += 1
            else:
                current_arg += character

        return args

    # primary command execution handler which returns a response (output or error)
    def execute(self, command, expected_args):
        args = self.parse_command(command, expected_args)
        if len(args) - 1 is not expected_args: return
        response = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return self.process_response(response)

    # process standard I/O
    def process_response(self, response):
        stdout, stderr = response.communicate()
        return stderr.rstrip().decode("utf-8") if stderr else stdout.rstrip().decode("utf-8")
