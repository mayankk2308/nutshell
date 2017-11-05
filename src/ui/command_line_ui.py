from appJar import gui
import nlu
import log_service

log = log_service.log_service()

def find_handler(output):
    output_destinations = ""
    line_number = 1
    for line in output:
        output_destinations += str(line_number) + ") " + line + "\n\n"
        line_number += 1
    log.write_data(output_destinations.strip())
    app.infoBox("Locations", output_destinations)


def open_handler(output):
    response = nlu.opencmd(output[0])
    log.write_data(response)
    app.infoBox("Response", response)


def copy_handler(output):
    src, dest = output
    response = nlu.copy_or_move("copy", src[0], dest[0])
    log.write_data(response)
    app.infoBox("Response", response)


def move_handler(output):
    src, dest = output
    response = nlu.copy_or_move("move", src[0], dest[0])
    log.write_data(response)
    app.infoBox("Response", response)


def rename_handler(output):
    src, new_name = output
    response = nlu.rename(src[0], new_name)
    log.write_data(response)
    app.infoBox("Response", response)


def organize_handler(output):
    src, doc_type = output
    response = nlu.organize(src[0], doc_type)
    log.write_data(response)
    app.infoBox("Response", response)


def request_handler(button):
    if button == "Submit":
        user_command = app.getEntry("Enter your Command: ");
        log.write_data(user_command)
        command_name, output = nlu.main(user_command)
        if output is None:
            app.infoBox("Error", command_name)
            log.write_data(command_name)
        elif command_name == "find":
            find_handler(output)

        elif command_name == "open":
            open_handler(output)

        elif command_name == "copy":
            copy_handler(output)

        elif command_name == "move":
            move_handler(output)

        elif command_name == "rename":
            rename_handler(output)

        elif command_name == "organize":
            organize_handler(output)

app = gui()
app.addLabel("Title", "Natural Language Unix")
app.addLabelEntry("Enter your Command: ")
app.addButtons(["Submit"], request_handler)
app.go()
