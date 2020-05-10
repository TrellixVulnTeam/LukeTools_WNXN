# global __lukescripts_local__
__lukescripts_local__ = True

nuke.tprint('LukeTools init.py')

if __lukescripts_local__:
    nuke.tprint('############### LUKE LOCAL MODE ON ###############')
    nuke.tprint('local LukeTools init.py')

    import L_callbacks
    nuke.addBeforeRender(L_callbacks.updateAllWriteNames)
    nuke.addBeforeRender(L_callbacks.enableOnRender)
    nuke.addKnobChanged(L_callbacks.updateWriteName, nodeClass="Write")

    import sr_rollingAutoSave

    nuke.addAutoSaveFilter( sr_rollingAutoSave.onAutoSave ) 
    nuke.addAutoSaveRestoreFilter( sr_rollingAutoSave.onAutoSaveRestore ) 
    nuke.addAutoSaveDeleteFilter( sr_rollingAutoSave.onAutoSaveDelete ) 

else:
    nuke.tprint('############### LUKE LOCAL MODE OFF ###############')

nuke.pluginAddPath('pixelfudger')
nuke.pluginAddPath('./higx/PointRender')

nuke.pluginAddPath('gizmos')

nuke.pluginAddPath('pythonlibrary')
