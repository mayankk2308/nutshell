//
//  CoreDataStack.swift
//  NLU
//
//  Created by Mayank Kumar on 2/26/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Foundation
import CoreData

class CoreDataStack {
    
    private static var instance: CoreDataStack!
    
    static func sharedInstance() -> CoreDataStack {
        if instance == nil {
            instance = CoreDataStack()
        }
        return instance
    }
    
    lazy var persistentContainer: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "NLU")
        container.loadPersistentStores(completionHandler: { (storeDescription, error) in
            if let error = error {
                fatalError("Unresolved error \(error)")
            }
        })
        return container
    }()
}
