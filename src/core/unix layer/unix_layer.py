import sys
from directory_service import MANAGEMENT_DIR
sys.path.append(MANAGEMENT_DIR)
from thread_manager import thread_manager
from log_service import log_service
from subprocess import Popen, PIPE
from output_codes import OCODE
from supported_commands import AVAILABLE_COMMANDS, EXPECTED_ARGS

class unix_manager(object):

    def __init__(self):
        self.logger = log_service()

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
            if character is " " and quotes % 2 is 0:
                args.append(current_arg)
                current_arg = ""
            elif character is "'":
                quotes += 1
            else:
                current_arg += character

        return args

    # primary command execution handler that calls back provided completion handler
    def execute(self, unix_command, completion_handler):
        self.logger.write_data("cmd: " + unix_command)
        args = self.parse_natural_command(unix_command.strip())
        instruction = args[0]
        args[0] = self.parse_to_std_command(args[0])
        if args[0] is None:
            self.logger.write_data("err: " + str(255) + " " + OCODE[255])
            completion_handler(255, OCODE[255])
            return
        if len(args) - 1 is not EXPECTED_ARGS[instruction]:
            self.logger.write_data("err: " + str(254) + " " + OCODE[254])
            completion_handler(254, OCODE[254])
            return
        response = Popen(args, stdout=PIPE, stderr=PIPE)
        error_code, response_message = self.process_response(response)
        self.logger.write_data(str(error_code) + " " + response_message)
        completion_handler(error_code, response_message)

    # process standard I/O
    def process_response(self, response):
        stdout, stderr = response.communicate()
        stdout = stdout.strip().decode("utf-8")
        stderr = stderr.strip().decode("utf-8")
        error_code = 1 if stderr else 0
        stdout = OCODE[0] if not stdout else stdout
        return (error_code, stderr if error_code is 1 else stdout)

    # explicit program termination notifier
    def terminate_unix_layer(self):
        self.logger.close_log()

    # destroy logging history
    def destroy_logs(self):
        self.logger.clear_all_logs()

# example + testing
manager = unix_manager()

def test_handler(error, message):
    print(error)
    print(message)

thread_manager = thread_manager()
thread_manager.background_exec(manager.execute, "open", test_handler)
manager.destroy_logs()
