from appJar import gui
import nlu


def findHandler(output):
    output_destinations = ""
    line_number = 1
    for line in output:
        output_destinations += str(line_number) + ") " + line + "\n\n"
        line_number += 1
    app.infoBox("Locations", output_destinations)


def openHandler(output):
    app.infoBox("Response", nlu.opencmd(output[0]))


def copyHandler(output):
    src, dest = output
    app.infoBox("Response", nlu.copy_or_move("copy", src[0], dest[0]))


def moveHandler(output):
    src, dest = output
    app.infoBox("Response", nlu.copy_or_move("move", src[0], dest[0]))


def renameHandler(output):
    src, new_name= output
    app.infoBox("Response", nlu.rename(src[0], new_name))


def organizeHandler(output):
    src, doc_type = output
    app.infoBox("Response", nlu.organize(src[0], doc_type))


def requestHandler(button):
    if button == "Submit":
        user_command = app.getEntry("Enter your Command: ");
        command_name, output = nlu.main(user_command)
        if output is None:
            app.infoBox("Error", command_name)

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
