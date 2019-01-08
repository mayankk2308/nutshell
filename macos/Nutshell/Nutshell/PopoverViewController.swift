//
//  PopoverViewController.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/5/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Cocoa

/// Defines Nutshell's primary user interface.
class PopoverViewController: NSViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do view setup here.
    }
    
    @IBAction func quit(_ sender: Any) {
        NSApplication.shared.terminate(sender)
    }
    
    @IBAction func showPreferences(_ sender: Any) {
        let appDel = NSApplication.shared.delegate as? AppDelegate
        appDel!.menuBarTool.popover.adjustPopoverHeight(by: 200)
    }
}
