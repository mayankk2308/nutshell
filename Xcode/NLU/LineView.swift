//
//  LineView.swift
//  NLU
//
//  Created by Mayank Kumar on 2/28/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Cocoa

class LineView: NSView {
    
    override func draw(_ dirtyRect: NSRect) {
        super.draw(dirtyRect)
        layer?.backgroundColor = NSColor.lightGray.cgColor
    }
    
}
