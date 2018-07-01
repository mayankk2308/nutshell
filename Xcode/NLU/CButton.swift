//
//  CButton.swift
//  NLU
//
//  Created by Mayank Kumar on 2/28/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Cocoa

enum CButtonType {
    case voice, settings, history, undo, add, go, report
}

class CButton: NSButton {

    private var buttonType: CButtonType!
    
    required init(frame frameRect: NSRect, buttonType type: CButtonType) {
        super.init(frame: frameRect)
        buttonType = type
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
    
    override func draw(_ dirtyRect: NSRect) {
        super.draw(dirtyRect)

        switch buttonType {
        case .voice:
            break
        case .settings:
            break
        case .history:
            break
        case .undo:
            break
        case .add:
            break
        case .go:
            break
        case .report:
            break
        default:
            break
        }
    }
    
}
