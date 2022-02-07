import os
from rv import commands
import PyOpenColorIO as OCIO

def ocio_config_from_media(media, attributes):

    if os.getenv("OCIO") == None:
        raise Exception("ERROR: $OCIO environment variable unset!")

    return OCIO.GetCurrentConfig()


def ocio_node_from_media(config, node, default, media=None, attributes={}):

    result = [{"nodeType": d, "context": {}, "properties": {}} for d in default]

    nodeType = commands.nodeType(node)

    if nodeType == "RVDisplayPipelineGroup":

        display = config.getDefaultDisplay()

        viewspace = os.environ.get("DISPLAY", "Rec.709")

        result = [
            {
                "nodeType": "OCIODisplay",
                "context": {},
                "properties": {
                    "ocio.function": "display",
                    "ocio.inColorSpace": OCIO.Constants.ROLE_SCENE_LINEAR,
                    "ocio_display.view": viewspace,
                    "ocio_display.display": display,
                },
            }
        ]

    elif nodeType == "RVLinearizePipelineGroup":

    
        inspace = config.parseColorSpaceFromString(media)
        
        if inspace == "":
            inspace = os.environ.get("COLORSPACE","")

        if inspace == "":
            if "exr" in media:
                inspace = "Output - Rec.709"
            if "jpg" in media or "jpeg" in media:
                inspace = "out_srgb"

        if inspace == "":
             inspace = config.getColorSpace(OCIO.Constants.ROLE_SCENE_LINEAR).getName()        

        if inspace != "":
            result = [
                {
                    "nodeType": "OCIOFile",
                    "context": {},
                    "properties": {
                        "ocio.function": "color",
                        "ocio.inColorSpace": inspace,
                        "ocio_color.outColorSpace": OCIO.Constants.ROLE_SCENE_LINEAR,
                    },
                },
                {"nodeType": "RVLensWarp", "context": {}, "properties": {}},
            ]

    elif nodeType == "RVLookPipelineGroup":
        # If our config has a Look named "shot_specific_look" and uses the
        # environment/context variable "$SHOT" to locate any required files
        # on disk, then this is what that would likely look like:
        #
        # result = [
        #     {"nodeType"   : "OCIOLook",
        #      "context"    : {"SHOT" : os.environ.get("SHOT", "def123")}
        #      "properties" : {
        #          "ocio.function"     : "look",
        #          "ocio.inColorSpace" : OCIO.Constants.ROLE_SCENE_LINEAR,
        #          "ocio_look.look"    : "shot_specific_look"}}]

        look = attributes.get("default_setting", "")
        if look != "":
            result = [
                {
                    "nodeType": "OCIOLook",
                    "context": {},
                    "properties": {"ocio.function": "look", "ocio_look.look": look},
                }
            ]

    return result