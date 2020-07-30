import nuke
import os
import L_callbacks
def L_newProject():

    pnode = False

    proot = 'K:/_VFX/'
    pproject = 'L'
    pshot = 'sh0100'
    ptask = 'comp'
    exists = False

    for n in nuke.allNodes():
        if n.name() == 'L_PROJECT':
            pnode = n
            proot = n['proot'].value()
            pproject = n['pproject'].value()
            pshot = n['pshot'].value()
            ptask = n['ptask'].value()
            exists = True
            break

    if not pnode:
        pnode = nuke.nodes.NoOp(name = "L_PROJECT")


    p = nuke.Panel('KLXR NEW PROJECT')
    p.addSingleLineInput('Root', proot)
    p.addSingleLineInput('Project', pproject)
    p.addSingleLineInput('Shot', pshot)
    p.addSingleLineInput('Task', ptask)

    p.setWidth(300)

    if exists:
        p.setTitle('PROJECT ALREADY EXISTS!')


    if p.show():

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
