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
    
    override func viewDidLoad() {
        super.viewDidLoad()
        commandTextField.focusRingType = .none
    }

}

