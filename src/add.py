# clink, v0.1.dev WIP
# (action-menu callback)

import dearpygui as dpg # type: ignore
import src.gui as gui

def add_to_actionlist(sender, app_data, user_data):
    gui.CONSOLE_BUFFER.append("Added to action-list: " + user_data)