//
//  main.swift
//  NLU
//
//  Created by Mayank Kumar on 2/26/18.
//  Copyright © 2018 Mayank Kumar. All rights reserved.
//

import Cocoa

guard let unixLayerPluginPath = Bundle.main.path(forResource: "UnixLayer", ofType: "plugin") else {
    fatalError("Bundle path for UnixLayer not found")
}

guard let unixLayerPluginBundle = Bundle(path: unixLayerPluginPath) else {
    fatalError("Unable to open bundle UnixLayer")
}

unixLayerPluginBundle.load()

guard let pClass = unixLayerPluginBundle.principalClass as? UnixLayerInterface.Type else {
    fatalError("Principal class could not be loaded")
}

_ = UnixLayer.instance(newInstance: pClass.instance())

exit(NSApplicationMain(CommandLine.argc, CommandLine.unsafeArgv))
