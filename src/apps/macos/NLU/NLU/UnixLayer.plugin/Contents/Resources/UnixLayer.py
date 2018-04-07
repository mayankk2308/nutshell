import objc
from Foundation import NSObject
from subprocess import Popen, PIPE
from OutputCodes import OCODE

UnixLayerInterface = objc.protocolNamed("NLU.UnixLayerInterface")

class UnixLayer(NSObject, protocols=[UnixLayerInterface]):

    @classmethod
    def instance(self):
        return UnixLayer.alloc().init()

    # parse command and extract expected arguments
    @objc.python_method
    def parseCommand(self, command):
        quotes = 0
        command += " "
        currentArg = ""
        args = []
        for character in command:
            if character is " " and quotes % 2 is 0:
                args.append(currentArg)
                currentArg = ""
            elif character is "'":
                quotes += 1
            else:
                currentArg += character

        return args

    # process standard I/O
    @objc.python_method
    def processResponse(self, response):
        stdout, stderr = response.communicate()
        error_code = response.returncode
        return (error_code, OCODE[error_code])

    def retrieveOutputMessageWithErrorCode_(self, errorCode):
        return OCODE[errorCode]

    # primary command execution handler that calls back provided completion handler
    def executeWithCommand_commandPaths_expectedArgs_completionHandler_(self, command, commandPaths, expectedArgs, completionHandler):
        args = self.parseCommand(command.strip())
        instruction = args[0]
        if instruction not in commandPaths.keys():
            completionHandler(255, OCODE[255])
            return
        if len(args) - 1 is not int(expectedArgs[instruction]):
            print("incorrect args")
            completionHandler(254, OCODE[254])
            return
        args[0] = commandPaths[instruction]
        if args[0] is "None":
            completionHandler(250, OCODE[250])
            return
        response = Popen(args, stdout=PIPE, stderr=PIPE)
        errorCode, responseMessage = self.processResponse(response)
        completionHandler(errorCode, responseMessage)
