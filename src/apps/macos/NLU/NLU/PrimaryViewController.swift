//
//  PrimaryViewController.swift
//  NLU
//
//  Created by Mayank Kumar on 2/26/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Cocoa

class PrimaryViewController: NSViewController {

    @IBOutlet weak var commandTextField: NSTextField!
    
    let ULM = UnixLayerManager()
    let LLM = LanguageLayerManager()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        commandTextField.focusRingType = .none
        commandTextField.textColor = color
//        LLM.request(withCommand: "move mydog.txt from Downloads to Trash") { error, message in
//            print(error)
//            print(message)
//        }
//        ULM.request(withCommand: "open /Applications", onCompletion: {error, message in
//            print(error)
//            print(message)
//        })
    }

}

