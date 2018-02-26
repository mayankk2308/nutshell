//
//  UnixLayerInterface.swift
//  NLU
//
//  Created by Mayank Kumar on 2/26/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Foundation


/// Primary Unix Layer interface
@objc public protocol UnixLayerInterface {
    
    
    /// Accesses an instance of the protocol from Python
    ///
    /// - Returns: instance of the protocol
    static func instance() -> UnixLayerInterface
    
    
    /// Find respective error message from code
    ///
    /// - Parameter errorCode: error code (between 0-255)
    /// - Returns: appropriate output message
    func retrieveOutputMessage(errorCode: Int) -> String
    
    /// Executes a unix command
    ///
    /// - Parameters:
    ///   - commandPath: path to the script
    ///   - completionHandler: handler for script completion
    ///   - errorCode: result error code
    ///   - response: result data
    /// - Returns: `Void`
    func execute(command: String, commandPaths: [String : String], expectedArgs: [String : Int], completionHandler: (_ errorCode: Int,_ response: String) -> Void) -> Void
    
}
