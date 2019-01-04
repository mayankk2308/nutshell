//
//  Language.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/4/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Foundation

/// Defines singleton instance mechanism for accessing Python-buit unix layer
class Language {
    
    
    /// Refers to the instance of the Python class
    private static var singleInstance: LanguageInterface!
    
    /// Access or set a new instance
    ///
    /// - Parameter newInstance: New instance to be set
    /// - Note: `newInstance` is optional and not required for access-only use
    /// - Returns: single instance available
    static func instance(newInstance: LanguageInterface? = nil) -> LanguageInterface {
        
        if singleInstance == nil && newInstance != nil {
            singleInstance = newInstance
        }
        return singleInstance
    }
    
}

