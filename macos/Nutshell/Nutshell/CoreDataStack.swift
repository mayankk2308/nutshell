//
//  CoreDataStack.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/4/19.
//  Copyright © 2019 MVTeam. All rights reserved.
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
        let container = NSPersistentContainer(name: "Nutshell")
        container.loadPersistentStores(completionHandler: { (storeDescription, error) in
            if let error = error {
                fatalError("Unresolved error \(error)")
            }
        })
        return container
    }()
}
