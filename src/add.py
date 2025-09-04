# clink, v0.1.dev WIP
# (action-menu callback)

import dearpygui as dpg # type: ignore
import src.gui as gui
import src.shared as sh

def add_to_actionlist(sender, app_data, user_data):
    # check if editing is allowed
    if sh.APP_ALLOW_EDITING == True:
        gui.CONSOLE_BUFFER.append("Added to action-list: " + user_data)
    else:
        # throw error message
        gui.CONSOLE_BUFFER.append("error_No Project loaded. Cannot add any objects.")