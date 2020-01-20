#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Convert to EXR
# COLOR: #b29100
#
#----------------------------------------------------------------------------------------------------------

import pyseq
writes = list()
for read in nuke.selectedNodes():
    seq = pyseq.img2pyseq(read["file"].value())
    if seq:
        write = nuke.nodes.Write()
        write["file_type"].setValue("exr")
        write.setInput(0,read)
        oldname = read["file"].value()
        oldext = oldname.split(".")[-1]
        write["file"].setValue(oldname.replace(oldext,"exr"))
        writes.append(write)