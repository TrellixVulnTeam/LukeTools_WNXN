import nuke
import os
import L_callbacks
def L_newProject():

    pnode = ""

    proot = 'E:/_VFX/'
    pproject = 'L'
    pshot = 'sh0100'
    ptask = 'comp'
    pCustomPrefix = ''
    pCustomPostfix = ''
    exists = False

    for n in nuke.allNodes():
        if n.name() == 'L_PROJECT':
            pnode = n
            proot = n['proot'].value()
            pproject = n['pproject'].value()
            pshot = n['pshot'].value()
            ptask = n['ptask'].value()
            if 'pCustomPrefix' in n.knobs():
                pCustomPrefix = n['pCustomPrefix'].value()

            if 'pCustomPostfix' in n.knobs():
                pCustomPostfix = n['pCustomPostfix'].value()
            exists = True
            break

    


    p = nuke.Panel('KLXR NEW PROJECT')
    p.addSingleLineInput('Root', proot)
    p.addSingleLineInput('Project', pproject)
    p.addSingleLineInput('Shot', pshot)
    p.addSingleLineInput('Task', ptask)
    p.addSingleLineInput('Custom Prefix', pCustomPrefix)
    p.addSingleLineInput('Custom Postfix', pCustomPostfix)
    p.addBooleanCheckBox('save new script?', False)

    p.setWidth(300)

    if exists:
        p.setTitle('PROJECT ALREADY EXISTS!')


    if p.show():
        
        if not pnode:
            pnode = nuke.nodes.NoOp(name = "L_PROJECT")

        proot = p.value('Root')
        pproject = p.value('Project')
        pshot = p.value('Shot')
        ptask = p.value('Task')
        pCustomPrefix = p.value('Custom Prefix')
        pCustomPostfix = p.value('Custom Postfix')

        psave = p.value('save new script?')


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
        pscriptname = pscripts

        if pCustomPrefix:
            pscriptname += pCustomPrefix + '_'

        pscriptname += pproject + '_' + pshot + '_' + ptask + '_v001.nk'

        if not os.path.isdir(pscripts) and psave:
            os.makedirs(pscripts)

        if exists:
            n['proot'].setValue(proot)
            n['pproject'].setValue(pproject)
            n['pshot'].setValue(pshot)
            n['ptask'].setValue(ptask)

            if 'pCustomPrefix' in n.knobs():
                n['pCustomPrefix'].setValue(pCustomPrefix)
                
            else:
                k = nuke.String_Knob("pCustomPrefix","Custom Prefix")
                k.setValue(pCustomPrefix)
                pnode.addKnob(k)

            if 'pCustomPostfix' in n.knobs():
                n['pCustomPostfix'].setValue(pCustomPostfix)
                
            else:
                k = nuke.String_Knob("pCustomPostfix","Custom Postfix")
                k.setValue(pCustomPostfix)
                pnode.addKnob(k)
            
        else:
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

            k = nuke.String_Knob("pCustomPrefix","Custom Prefix")
            k.setValue(pCustomPrefix)
            pnode.addKnob(k)

            k = nuke.String_Knob("pCustomPostfix","Custom Postfix")
            k.setValue(pCustomPostfix)
            pnode.addKnob(k)

            k = nuke.Boolean_Knob("pMarmalade","Marmalade Mode")
            k.setValue(False)
            k.setFlag(nuke.STARTLINE)
            pnode.addKnob(k)

        if psave:
            nuke.scriptSaveAs(pscriptname)