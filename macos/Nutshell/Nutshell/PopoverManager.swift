//
//  PopoverManager.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/7/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Cocoa

extension NSPopover {
    
    func adjustPopoverHeight(by heightOffset: CGFloat) {
        contentSize.height += heightOffset
        contentViewController?.view.frame.size.height += heightOffset
    }
}
