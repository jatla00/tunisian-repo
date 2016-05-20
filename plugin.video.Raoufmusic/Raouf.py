# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates, Guides & Merlin Tube
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from YouTube & Merlin Tube addons
#
# Thanks To: Merlin
# Author:    Merlin
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.merlinmusic'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# aflam arabe
YOUTUBE_PLAYLIST_ID_1 = "PLKMOKg8CbJ7HVrZC6NdOIbjFaHvALkEOY"			#buffalo
YOUTUBE_PLAYLIST_ID_2 = "PLTAMhu2e0NlgVpfEvvEl46PW0Bg9GJt0X"			#buffalo

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR blue][B]كنب ادب مسموعة[/B][/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_PLAYLIST_ID_2+"/",
        thumbnail="special://home/addons/plugin.video.merlinmusic/resources/music1.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR blue][B]أفلام عربية[/B][/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_PLAYLIST_ID_1+"/",
        thumbnail="special://home/addons/plugin.video.merlinmusic/resources/musicb.png",
        folder=True )

run()