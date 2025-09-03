# clink v0.1.dev

import sys
sys.dont_write_bytecode = True  # disable __pycache__ globally
import platform # environment checks
import dearpygui.dearpygui as dpg # type: ignore
import dearpygui # type: ignore
from src.gui import display_gui
from src.gui import add_to_console
import src.gui as gui
import src.gui_ids as id

def run():
    # check the current system environment
    current_platform = platform.system()
    render_api = "misc"
    if current_platform == "Windows":
        render_api = "DX11"
    elif current_platform == "Darwin" or current_platform == "Linux":
        render_api = "GL"

    dpg.create_context()


    # load gui
    display_gui()

    gui.CONSOLE_BUFFER.append("clink studio v0.1.dev - https://github.com/schmalzl/clink")
    gui.CONSOLE_BUFFER.append("(c) 2025 Kian Schmalzl")
    

    # define window styles
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

    with dpg.theme() as console_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 5, 0)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 2, 0)
    


    # apply styles
    dpg.bind_theme(global_theme)
    dpg.bind_item_theme(id._console_win, console_theme)

    # set title
    app_title = "clink studio 0.1.dev <" + render_api + ">"

    dpg.create_viewport(title=app_title, width=1000, height=800, resizable=False)
    # set window icon
    dpg.set_viewport_large_icon("./assets/icons/icon_128.ico")

    dpg.setup_dearpygui()
    dpg.show_viewport()

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        
        # --- custom code ---
        add_to_console()
        


    dpg.destroy_context()

if __name__ == "__main__":
    run()