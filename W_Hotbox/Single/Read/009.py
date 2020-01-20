#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Check EXR
# COLOR: #660547
#
#----------------------------------------------------------------------------------------------------------

for read in nuke.allNodes("Read"):
    error = ""
    if read["file"].value().endswith("exr"):
        if read.metadata()["exr/channels"] not in ("A:{1 0 1 1},B:{1 0 1 1},G:{1 0 1 1},R:{1 0 1 1}", "B:{1 0 1 1},G:{1 0 1 1},R:{1 0 1 1}"):
            error += "channels dont match multipart description"
        if read.metadata()["input/bitsperchannel"] == "32-bit float":
            error += "\n32 bit float"
        
        if error:
            error += "\nTHIS IS PROBABLY NO MULTIPART IMAGE SUPER SLOW PLEASE CONVERT"
            read["label"].setValue(error)
            read["note_font_size"].setValue(30)