from appJar import gui
import nlu
import log_service

log = log_service.log_service()

def findHandler(output):
    output_destinations = ""
    line_number = 1
    for line in output:
        output_destinations += str(line_number) + ") " + line + "\n\n"
        line_number += 1
    log.write_data(output_destinations.strip())
    app.infoBox("Locations", output_destinations)


def openHandler(output):
    response = nlu.opencmd(output[0])
    log.write_data(response)
    app.infoBox("Response", response)


def copyHandler(output):
    src, dest = output
    response = nlu.copy_or_move("copy", src[0], dest[0])
    log.write_data(response)
    app.infoBox("Response", response)


def moveHandler(output):
    src, dest = output
    response = nlu.copy_or_move("move", src[0], dest[0])
    log.write_data(response)
    app.infoBox("Response", response)


def renameHandler(output):
    src, new_name = output
    response = nlu.rename(src[0], new_name)
    log.write_data(response)
    app.infoBox("Response", response)


def organizeHandler(output):
    src, doc_type = output
    response = nlu.organize(src[0], doc_type)
    log.write_data(response)
    app.infoBox("Response", response)


def requestHandler(button):
    if button == "Submit":
        user_command = app.getEntry("Enter your Command: ");
        log.write_data(user_command)
        command_name, output = nlu.main(user_command)
        if output is None:
            app.infoBox("Error", command_name)
            log.write_data(command_name)
        elif command_name == "find":
            findHandler(output)

        elif command_name == "open":
            openHandler(output)

        elif command_name == "copy":
            copyHandler(output)

        elif command_name == "move":
            moveHandler(output)

        elif command_name == "rename":
            renameHandler(output)

        elif command_name == "organize":
            organizeHandler(output)

app = gui()
app.addLabel("Title", "Natural Language Unix")
app.addLabelEntry("Enter your Command: ")
app.addButtons(["Submit"], requestHandler)
app.go()
