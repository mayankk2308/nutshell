//
//  LanguageLayer.swift
//  NLU
//
//  Created by Mayank Kumar on 4/13/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Foundation


/// Defines singleton instance mechanism for accessing Python-buit unix layer
class LanguageLayer {
    
    
    /// Refers to the instance of the Python class
    private static var singleInstance: LanguageLayerInterface!
    
    
    /// Access or set a new instance
    ///
    /// - Parameter newInstance: New instance to be set
    /// - Note: `newInstance` is optional and not required for access-only use
    /// - Returns: single instance available
    static func instance(newInstance: LanguageLayerInterface? = nil) -> LanguageLayerInterface {
        
        if singleInstance == nil && newInstance != nil {
            singleInstance = newInstance
        }
        return singleInstance
    }
    
}
