//
//  UnixLayer.swift
//  NLU
//
//  Created by Mayank Kumar on 2/26/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Foundation


/// Defines singleton instance mechanism for accessing Python-buit unix layer
class UnixLayer {
    
    
    /// Refers to the instance of the Python class
    private static var singleInstance: UnixLayerInterface!
    
    
    /// Access or set a new instance
    ///
    /// - Parameter newInstance: New instance to be set
    /// - Note: `newInstance` is optional and not required for access-only use
    /// - Returns: single instance available
    static func instance(newInstance: UnixLayerInterface? = nil) -> UnixLayerInterface {
        
        if singleInstance == nil && newInstance != nil {
            singleInstance = newInstance
        }
        return singleInstance
    }
    
}
