//
//  MenuBarTool.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/5/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Cocoa

/// Defines the Nutshell menubar item
class MenuBarTool {
    
    let statusItem = NSStatusBar.system.statusItem(withLength: NSStatusItem.squareLength)
    
    let popover = NSPopover()
    
    /// Responsible for setting up the menu bar item.
    func prepareMenuBarTool() {
        popover.contentViewController = PopoverViewController()
        if let button = statusItem.button {
            button.image = NSImage(named: NSImage.Name("MenuBarIcon"))
            button.target = self
            button.action = #selector(togglePopover(_:))
        }
    }
    
    /// Handles the popover view presentation.
    ///
    /// - Parameter sender: Object responsible for the action.
    @objc func togglePopover(_ sender: Any?) {
        if popover.isShown {
            popover.performClose(sender)
        } else {
            if let button = statusItem.button {
                popover.show(relativeTo: button.bounds, of: button, preferredEdge: .minY)
            }
        }
    }
}
