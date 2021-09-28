# import logging

# logger = logging.getLogger('Luke init')
# logger.setLevel('DEBUG')
# stderr_log_handler = logging.StreamHandler()
# logger.addHandler(stderr_log_handler)
# stderr_log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

nuke.tprint('LukeTools init.py')

if __lukescripts_local__:
    nuke.tprint('############### LUKE LOCAL MODE ON ###############')
    nuke.tprint('local LukeTools init.py')

    import L_callbacks
    nuke.addBeforeRender(L_callbacks.updateAllWriteNames)
    nuke.addBeforeRender(L_callbacks.enableOnRender)
    # nuke.addKnobChanged(L_callbacks.updateWriteName, nodeClass="Write")
    # nuke.addOnCreate(L_callbacks.writeNodeFields, nodeClass= "Write")


    import sr_rollingAutoSave
    nuke.addAutoSaveFilter( sr_rollingAutoSave.onAutoSave ) 
    nuke.addAutoSaveRestoreFilter( sr_rollingAutoSave.onAutoSaveRestore ) 
    nuke.addAutoSaveDeleteFilter( sr_rollingAutoSave.onAutoSaveDelete ) 

else:
    nuke.tprint('############### LUKE LOCAL MODE OFF ###############')

# Higx
nuke.pluginAddPath('./higx/PointRender')

#pgBokeh
nuke.pluginAddPath('pgBokeh')

# Gizmos
nuke.pluginAddPath('gizmos')
nuke.pluginAddPath('pixelfudger')
# nuke.pluginAddPath( './gizmos/bm_NukeTools' )
# nuke.pluginAddPath( 'cryptomatte' )

# Icons
nuke.pluginAddPath('icons')

# Gradient Editor
# nuke.pluginAddPath('./GradientEditor')
# nuke.pluginAddPath('./GradientEditor/icons')
# nuke.pluginAddPath('./GradientEditor/tools')
# nuke.pluginAddPath('./GradientEditor/grapichs')
# nuke.pluginAddPath('./GradientEditor/python')

# AutoFlare
nuke.pluginAddPath('AutoFlare')
nuke.pluginAddPath('./AutoFlare/BOKEHS')
nuke.pluginAddPath('./AutoFlare/BOKEHS/polygons')


# nuke.pluginAddPath('rv_ocio')

