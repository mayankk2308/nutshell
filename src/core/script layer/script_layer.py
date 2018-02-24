from subprocess import Popen, PIPE
from supported_commands import AVAILABLE_COMMANDS, EXPECTED_ARGS

class script_manager(object):

    # retrieve appropriate command
    def parse_to_std_command(self, unix_command):
        return AVAILABLE_COMMANDS[unix_command] if unix_command in AVAILABLE_COMMANDS.keys() else None

    # parse command and extract expected arguments
    def parse_natural_command(self, unix_command):
        quotes = 0
        unix_command += " "
        current_arg = ""
        args = []
        for character in unix_command:
            if character is " " and quotes % 2 == 0:
                args.append(current_arg)
                current_arg = ""
            elif character is "'":
                quotes += 1
            else:
                current_arg += character

        return args

    # primary command execution handler that calls back provided completion handler
    def execute(self, unix_command, completion_handler):
        args = self.parse_natural_command(unix_command.strip())
        instruction = args[0]
        args[0] = self.parse_to_std_command(args[0])
        if args[0] is None:
            return (255, "This command is invalid or not currently supported.")
        if len(args) - 1 is not EXPECTED_ARGS[instruction]:
            return (254, "Invalid arguments provided for command. Please recheck your input.")
        response = Popen(args, stdout=PIPE, stderr=PIPE)
        error_code, response_message = self.process_response(response)
        completion_handler(error_code, response_message)

    # process standard I/O
    def process_response(self, response):
        stdout, stderr = response.communicate()
        stdout = stdout.strip().decode("utf-8")
        stderr = stderr.strip().decode("utf-8")
        error_code = 1 if stderr else 0
        stdout = "Action successful." if not stdout else stdout
        return (error_code, stderr if error_code is 1 else stdout)

# example
manager = script_manager()

def test_handler(error, message):
    print(error)
    print(message)
    
manager.execute("open '/Applications'", test_handler)
