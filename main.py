# clink, v0.1.dev WIP - https://github.com/schmalzl/clink
# Copyright (c) 2025 Kian Schmalzl
# (program main entry point)

# sys import for pycache deactivation
import sys
# disable __pycache__ creation globally
sys.dont_write_bytecode = True

# --- Main includes
# import enviroment check with platform.system()
import platform
# import dear pygui (ui library)
import dearpygui.dearpygui as dpg # type: ignore
import dearpygui # type: ignore
# import functions to load gui and update internal console
from src.gui import load_gui
from src.gui import add_to_console
import src.gui as gui
# shared package for specific container theme (console)
import src.gui_ids as id
import src.shared as sh

def run():
    # check current system environment (Windows, Mac, Linux)
    current_platform = platform.system()
    render_api = "misc"
    if current_platform == "Windows":
        # DirectX 11 backend
        render_api = "DX11"
    elif current_platform == "Darwin" or current_platform == "Linux":
        # OpenGL backend
        render_api = "GL"


    dpg.create_context()    # create dear pygui context
    load_gui()              # load gui from gui.py

    # add startup message to console buffer
    gui.CONSOLE_BUFFER.append("clink studio v0.1.dev - https://github.com/schmalzl/clink")
    gui.CONSOLE_BUFFER.append("(c) 2025 Kian Schmalzl")


    # define global window style and color scheme
    # Note: Other style variables can be added or changed for further customization
    #       Please refer to https://dearpygui.readthedocs.io/en/latest/documentation/themes.html
    #       for further information.
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 5, 5)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 2, 3)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 1)
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (27, 27, 27))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (40, 40, 40))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (40, 40, 40))

    # define console-specific window style
    with dpg.theme() as console_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 5, 0)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 2, 0)

    # apply styles
    dpg.bind_theme(global_theme)                        # global
    dpg.bind_item_theme(id._console_win, console_theme) # console specific


    # set title and create viewport
    app_title = "clink studio 0.1.dev <" + render_api + ">"
    dpg.create_viewport(title=app_title, width=1000, height=800, resizable=False)
    
    # set window icon
    dpg.set_viewport_large_icon("./assets/icons/icon_128.ico")

    dpg.setup_dearpygui()   # setup viewport
    dpg.show_viewport()     # show viewport

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        # console update every frame until loop closed
        add_to_console()
        gui.update_values()

        # check if a project is currently loaded and set is_project_active=True to allow editing
        if sh.APP_CURRENT_PROJECT != "No open project.":
            sh.APP_ALLOW_EDITING = True
        else:
            sh.APP_ALLOW_EDITING = False
    
    # --- program will stop here until the window is closed ---
    # POST COMMAND EXECUTIONS
    dpg.destroy_context()   # destroy dear pygui context

if __name__ == "__main__":
    run()