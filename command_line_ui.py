from appJar import gui
import nlu

def handleFind(response):
    if response == 0:
        app.scr
        app.infoBox("Error", "File/Folder not found")
    else:
        ctr = 1
        output = ""
        for option in response:
            output += str(ctr) +")" + " " + option + "\n\n"
            ctr += 1
        app.infoBox("File Path List",output)

def requestHandler(button):
    if button == "Submit":
        request = app.getEntry("Enter your Command: ")
        command,response = nlu.main(request)
        if command == "find":
            handleFind(response)

app = gui()
app.addLabel("Title", "Natural Language Unix")
app.addLabelEntry("Enter your Command: ")
app.addButtons(["Submit"], requestHandler)
app.go()
