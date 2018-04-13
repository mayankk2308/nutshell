//
//  LanguageLayerManager.swift
//  NLU
//
//  Created by Mayank Kumar on 4/13/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Foundation


/// Primary Unix Layer interaction management gateway
class LanguageLayerManager {
    
    private let languageLayer = LanguageLayer.instance()
    
    /// Handles requests to the Python unix layer
    ///
    /// - Parameters:
    ///   - command: command to execute
    ///   - completionHandler: escaping handler for script completion
    ///   - errorCode: error code on script completion
    ///   - response: result message on script completion
    func request(withCommand command: String, onCompletion completionHandler: (_ errorCode: Int,_ response: [String]) -> Void) {
        languageLayer.parse(command: command, completionHandler: completionHandler)
    }
    
}
