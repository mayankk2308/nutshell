//
//  ScriptResourceManager.swift
//  NLU
//
//  Created by Mayank Kumar on 2/26/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Foundation


/// Manages paths to script resources
class ScriptResourceManager {
    
    /// Stores commands that are unix-redundant
    private static let redundantCommandMatches = [
        "rename": "move"
    ]
    
    
    /// Stores expected arguments for commands
    static let expectedArgs = [
        "open": 1,
        "find": 1,
        "copy": 2,
        "move": 2,
        "rename": 2,
        "organize": 2
    ]
    
    /// Retrieves the path for requested script from the bundle
    ///
    /// - Parameter command: requested command
    /// - Returns: path of the script
    private static func retrieveCommandPath(forCommand command: String) -> String? {
        var cmd = command
        if let rCmd = redundantCommandMatches[cmd] {
            cmd = rCmd
        }
        guard let path = Bundle.main.path(forResource: cmd, ofType: "sh") else {
            return nil
        }
        return path
    }
    
    
    /// Retrieves script paths for commands
    ///
    /// - Returns: a mapping from command to script path
    static func allCommandPaths() -> [String : String] {
        return [
            "open": retrieveCommandPath(forCommand: "open") ?? "None",
            "copy": retrieveCommandPath(forCommand: "copy") ?? "None",
            "find": retrieveCommandPath(forCommand: "find") ?? "None",
            "move": retrieveCommandPath(forCommand: "move") ?? "None",
            "rename": retrieveCommandPath(forCommand: "move") ?? "None",
            "organize": retrieveCommandPath(forCommand: "organize") ?? "None",
        ]
    }
    
}
