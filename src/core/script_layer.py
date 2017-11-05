import subprocess
import os
from supported_commands import AVAILABLE_COMMANDS

class script_manager(object):

    # retrieve appropriate command
    def parse_to_std_command(self, command):
        return AVAILABLE_COMMANDS[command]

    # parse command and extract expected arguments
    def parse_natural_command(self, natural_command):
        quotes = 0
        natural_command += " "
        current_arg = ""
        arg_count = -1
        args = []
        for character in natural_command:
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
    def execute(self, natural_command, expected_args):
        args = self.parse_natural_command(natural_command)
        if len(args) - 1 is not expected_args: return "Invalid arguments."
        args[0] = self.parse_to_std_command(args[0])
        response = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = self.process_response(response)
        print(output)
        return "Failed to retrieve output. An error occurred." if output is None else output

    # process standard I/O
    def process_response(self, response):
        stdout, stderr = response.communicate()
        return stderr.rstrip().decode("utf-8") if stderr else stdout.rstrip().decode("utf-8")
