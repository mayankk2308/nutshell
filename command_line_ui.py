from appJar import gui
import nlu


def reset_box():
    app.removeAllWidgets()
    app.addLabel("Title", "Natural Language Unix")
    app.addLabelEntry("Enter your Command: ")
    app.addButtons(["Submit"], requestHandler)


def radiochoice(rb):
    user = app.getRadioButton("option")
    reset_box()
    app.infoBox("Response", nlu.opencmd(user))

def radioHandler(options):
    for item in options:
        app.addRadioButton("option", item)
    app.addButtons(["Choose"], radiochoice)

def findHandler(output):
    output_destinations = ""
    line_number = 1
    for line in output:
        output_destinations += str(line_number) + ") " + line + "\n\n"
        line_number += 1
    app.infoBox("Locations", output_destinations)

def openHandler(output):

    if len(output) == 1:
        app.infoBox("Response", nlu.opencmd(output[0]))
    else:
        radioHandler(output)


def requestHandler(button):
    if button == "Submit":
        user_command = app.getEntry("Enter your Command: ");
        command_name, output = nlu.main(user_command)
        if output is None:
            app.infoBox("Error", command_name)

        if command_name == "find":
            findHandler(output)

        elif command_name == "open":
            openHandler(output)


app = gui()
app.addLabel("Title", "Natural Language Unix")
app.addLabelEntry("Enter your Command: ")
app.addButtons(["Submit"], requestHandler)
app.go()
