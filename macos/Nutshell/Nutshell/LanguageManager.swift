//
//  LanguageManager.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/4/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Foundation

/// Primary language interaction management gateway
class LanguageManager {
    
    private let language = Language.instance()
    
    /// Handles requests to the Python unix layer
    ///
    /// - Parameters:
    ///   - command: command to execute
    ///   - completionHandler: escaping handler for script completion
    ///   - errorCode: error code on script completion
    ///   - response: result message on script completion
    func request(withCommand command: String, onCompletion completionHandler: (_ errorCode: Int,_ response: [String]) -> Void) {
        language.parse(command: command, completionHandler: completionHandler)
    }
    
}
