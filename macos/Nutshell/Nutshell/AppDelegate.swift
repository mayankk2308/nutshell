//
//  AppDelegate.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/4/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Cocoa

class AppDelegate: NSObject, NSApplicationDelegate {
    
    let menuBarTool = MenuBarTool()
    
    func applicationWillFinishLaunching(_ notification: Notification) {
        menuBarTool.prepareMenuBarTool()
    }
    
    func applicationDidFinishLaunching(_ aNotification: Notification) {
    }
    
    func applicationWillTerminate(_ aNotification: Notification) {
    }
    
    func windowWillReturnUndoManager(window: NSWindow) -> UndoManager? {
        return CoreDataStack.sharedInstance().persistentContainer.viewContext.undoManager
    }
    
    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
        let context = CoreDataStack.sharedInstance().persistentContainer.viewContext
        if !context.commitEditing() {
            NSLog("\(NSStringFromClass(type(of: self))) unable to commit editing to terminate")
            return .terminateCancel
        }
        if !context.hasChanges {
            return .terminateNow
        }
        do {
            try context.save()
        } catch {
            let nserror = error as NSError
            
            let result = sender.presentError(nserror)
            if (result) {
                return .terminateCancel
            }
            
            let question = NSLocalizedString("Could not save changes while quitting. Quit anyway?", comment: "Quit without saves error question message")
            let info = NSLocalizedString("Quitting now will lose any changes you have made since the last successful save", comment: "Quit without saves error question info");
            let quitButton = NSLocalizedString("Quit anyway", comment: "Quit anyway button title")
            let cancelButton = NSLocalizedString("Cancel", comment: "Cancel button title")
            let alert = NSAlert()
            alert.messageText = question
            alert.informativeText = info
            alert.addButton(withTitle: quitButton)
            alert.addButton(withTitle: cancelButton)
            
            let answer = alert.runModal()
            if answer == .alertSecondButtonReturn {
                return .terminateCancel
            }
        }
        return .terminateNow
    }
    
}
