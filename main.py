# clink v0.1.dev

import sys
sys.dont_write_bytecode = True  # disable __pycache__ globally
import platform # environment checks
import dearpygui.dearpygui as dpg # type: ignore
import dearpygui # type: ignore
from src.gui import display_gui
from src.console import add_to_console


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

# add startup message to console buffer
add_to_console("clink studio v0.1.dev - https://github.com/schmalzl/clink")
add_to_console("(c) 2025 Kian Schmalzl")

# define window styles
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
       dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0)
       dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0)
       dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 5, 5)
       dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 2, 3)
       dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 1)

# apply styles
dpg.bind_theme(global_theme)

# set title
app_title = "clink studio 0.1.dev <" + render_api + ">"

dpg.create_viewport(title=app_title, width=1000, height=800, resizable=False)
# set window icon
dpg.set_viewport_large_icon("./assets/icons/icon_128.ico")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()