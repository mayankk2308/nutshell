//
//  main.swift
//  Nutshell
//
//  Created by Mayank Kumar on 1/4/19.
//  Copyright © 2019 MVTeam. All rights reserved.
//

import Cocoa

guard let languagePluginPath = Bundle.main.path(forResource: "CkyParser", ofType: "plugin") else {
    fatalError("Bundle path for CkyParser not found")
}

guard let languagePluginBundle = Bundle(path: languagePluginPath) else {
    fatalError("Unable to open bundle CkyParser")
}

languagePluginBundle.load()

guard let pLanguageClass = languagePluginBundle.principalClass as? LanguageInterface.Type else {
    fatalError("Principal class could not be loaded")
}

_ = Language.instance(newInstance: pLanguageClass.instance())

exit(NSApplicationMain(CommandLine.argc, CommandLine.unsafeArgv))

