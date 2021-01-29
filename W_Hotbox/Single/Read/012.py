#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Consolidate Seq
#
#----------------------------------------------------------------------------------------------------------

import mvNamingApi
import pyseq
import mvNamingApi.utils

namingApi = mvNamingApi.get_api()


for node in nuke.selectedNodes():

    seq = pyseq.img2pyseq(node["file"].value())
    templ = namingApi.template_from_path(seq.path())
    if templ:
        fields = namingApi.fields_from_path(seq.path(),templ)
        
        if "rLayer" not in fields:
            fields["rLayer"] = "consolidate"
        else:
            fields["rLayer"] = "%s-consolidate" % fields.get("rLayer")
            
        task = nuke.ProgressTask('consolidate image sequence %s' % node.name() )
        
        for e,image in enumerate(seq.getAllItems()):   
            frame = seq.start()+e
            fields["frame"] = frame
            outPath = namingApi.apply_fields(fields,templ)
            print image
            print outPath
            mvNamingApi.utils.copyfile(image.path,outPath)#
            task.setMessage( 'processing frame %s' % frame )
            task.setProgress( int( float(e+1) / len(seq) *100) )
    else:
        nuke.message("Filename not NC conform cannot consolidate %s" % node.name())
        