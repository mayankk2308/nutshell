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
        "open_command": 1,
        "find_command": 1,
        "copy_command": 2,
        "move_command": 2,
        "rename_command": 2,
        "organize_command": 2
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
            "open_command": retrieveCommandPath(forCommand: "open") ?? "None",
            "copy_command": retrieveCommandPath(forCommand: "copy") ?? "None",
            "find_command": retrieveCommandPath(forCommand: "find") ?? "None",
            "move_command": retrieveCommandPath(forCommand: "move") ?? "None",
            "rename_command": retrieveCommandPath(forCommand: "move") ?? "None",
            "organize_command": retrieveCommandPath(forCommand: "organize") ?? "None",
        ]
    }
    
}
