import subprocess
import os

class script_manager(object):

    def parse_command(self, command, expected_args):
        # string parsing
        quotes = 0
        current_arg = ""
        arg_count = -1
        script, args = "", []
        for character in command:
            if character is " " and quotes % 2 == 0:
                # print(current_arg)
                arg_count += 1
                if arg_count == 0:
                    script = current_arg
                else:
                    args.append(current_arg)
                current_arg = ""
            elif character is "\"":
                quotes += 1
            else:
                current_arg += character

        return (script, args)

    def execute(self, command, expected_args):
        # primary command execution
        script, args = self.parse_command(command, expected_args)
        if len(args) is not expected_args: return
        print(script)
        print(args)
