//
//  LanguageLayerInterface.swift
//  NLU
//
//  Created by Mayank Kumar on 4/13/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Foundation

/// Primary Unix Layer interface
@objc public protocol LanguageLayerInterface {
    
    
    /// Accesses an instance of the protocol from Python
    ///
    /// - Returns: instance of the protocol
    static func instance() -> LanguageLayerInterface
    
    /// Find respective error message from code
    ///
    /// - Parameter errorCode: error code (between 0-255)
    /// - Returns: appropriate output message
//    func retrieveOutputMessage(errorCode: Int) -> String
    
    /// Executes a unix command
    ///
    /// - Parameters:
    ///   - commandPath: path to the script
    ///   - completionHandler: handler for script completion
    /// - Returns: `Void`
    func parse(command: String, completionHandler: (_ error: Int,_ response: [String]) -> Void) -> Void
    
}
