//
//  PrimaryWindowController.swift
//  NLU
//
//  Created by Mayank Kumar on 2/26/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Cocoa

class PrimaryWindowController: NSWindowController {
    
    override func windowDidLoad() {
        super.windowDidLoad()
        
        if let window = window {
            window.titlebarAppearsTransparent = true
        }
    }

}
