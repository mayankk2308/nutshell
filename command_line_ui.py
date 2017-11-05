from appJar import gui
import nlu

command = None
user = None
def reset_box():
    app.removeAllWidgets()
    app.addLabel("Title", "Natural Language Unix")
    app.addLabelEntry("Enter your Command: ")
    app.addButtons(["Submit"], requestHandler)


def radiochoice(rb):
    if command == "open":
        user = app.getRadioButton("option")
        reset_box()
        app.infoBox("Response", nlu.opencmd(user))

    else:
        global user
        user = app.getRadioButton("option")

def radiochoice1(rb):
        global user
        user2 = app.getRadioButton("option1")
        print("The command is:",command,user,user2)

def radioHandler(options):
    if command == "open":
        for item in options:
            app.addRadioButton("option", item)
        app.addButtons(["Choose"], radiochoice)

    else:
        for item in options[0]:
            app.addRadioButton("option", item)
        app.addButtons(["Choose"], radiochoice)

        for item in options[1]:
            app.addRadioButton("option1", item)
        app.addButtons(["ChooseSecond"], radiochoice1)



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
        global command
        command = "open"
        radioHandler(output)

def copyHandler(output):
    radioHandler(output)

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

        else:
            global command
            command = command_name
            copyHandler(output)


app = gui()
app.addLabel("Title", "Natural Language Unix")
app.addLabelEntry("Enter your Command: ")
app.addButtons(["Submit"], requestHandler)
app.go()
