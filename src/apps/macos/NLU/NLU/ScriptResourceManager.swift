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
    private let redundantCommandMatches = [
        "rename": "move"
    ]
    
    /// Retrieves the path for requested script from the bundle
    ///
    /// - Parameter command: requested command
    /// - Returns: path of the script
    func retrieveCommandPath(forCommand command: String) -> String? {
        var cmd = command
        if let rCmd = redundantCommandMatches[cmd] {
            cmd = rCmd
        }
        guard let path = Bundle.main.path(forResource: cmd, ofType: "sh") else {
            return nil
        }
        return path
    }
    
}
