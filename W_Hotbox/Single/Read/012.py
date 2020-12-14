#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: create EXR Write
# COLOR: #b29100
#
#----------------------------------------------------------------------------------------------------------

import pythonlibrary.L_pyseq as L_pyseq
writes = list()
for read in nuke.selectedNodes():
    seq = L_pyseq.img2pyseq(read["file"].value())
    if seq:
        write = nuke.nodes.Write()
        write["file_type"].setValue("exr")
        write.setInput(0,read)
        oldname = read["file"].value()
        oldext = oldname.split(".")[-1]
        write["file"].setValue(oldname.replace(oldext,"exr"))
        writes.append(write)