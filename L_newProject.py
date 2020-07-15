import nuke
import os
import L_callbacks
def L_newProject():

    p = nuke.Panel('KLXR NEW PROJECT')
    p.addSingleLineInput('Root', 'K:/_VFX/')
    p.addSingleLineInput('Project', 'L')
    p.addSingleLineInput('Shot','sh0100')
    p.addSingleLineInput('Task','comp')

    p.show()

    proot = p.value('Root')
    pproject = p.value('Project')
    pshot = p.value('Shot')
    ptask = p.value('Task')


    if proot == '':
        nuke.message('No Root')
        return    
    if pproject == '':
        nuke.message('No Project')
        return
    if pshot == '':
        nuke.message('No Shot')
        return
    if ptask == '':
        nuke.message('No Task')
        return

    pfolder = proot + pproject+'/'+pshot+'/'

    pscripts = pfolder+'scripts/'
    pscriptname = pscripts + pproject + '_' + pshot + '_' + ptask + '_v001.nk'

    if not os.path.isdir(pscripts):
        os.makedirs(pscripts)
    nuke.scriptSaveAs(pscriptname)

    write = nuke.createNode('Write', inpanel = False)

    pnode = nuke.nodes.NoOp(name = "L_PROJECT")
    pnode.setXpos(write.xpos() + 300)
    pnode.setYpos(write.ypos() + 200)

    k = nuke.File_Knob("proot","Root")
    k.setValue(proot)
    pnode.addKnob(k)

    k = nuke.String_Knob("pproject","Project")
    k.setValue(pproject)
    pnode.addKnob(k)

    k = nuke.String_Knob("pshot","Shot")
    k.setValue(pshot)
    pnode.addKnob(k)

    k = nuke.String_Knob("ptask","Task")
    k.setValue(ptask)
    pnode.addKnob(k)
