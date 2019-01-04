//
//  LanguageInterface.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/4/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Foundation

/// Primary Unix Layer interface
@objc public protocol LanguageInterface {
    
    
    /// Accesses an instance of the protocol from Python
    ///
    /// - Returns: instance of the protocol
    static func instance() -> LanguageInterface
    
    /// Parses a command
    ///
    /// - Parameters:
    ///   - commandPath: plaintext command
    ///   - completionHandler: handler for parse completion
    /// - Returns: `Void`
    func parse(command: String, completionHandler: (_ error: Int,_ response: [String]) -> Void) -> Void
    
}
