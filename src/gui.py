# clink, v0.1.dev WIP
# (gui code and console handler)

# dear pygui framework
import dearpygui.dearpygui as dpg # type: ignore

from src.add import add_to_actionlist
import src.menu_callbacks as cb     # menu callbacks for viewport menu bar
import src.gui_ids as id            # shared module
import src.shared as var            # shared global variables 

# Console log buffer
CONSOLE_BUFFER = []

def load_gui():
    # viewport menu bar
    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New Project")
            dpg.add_menu_item(label="Open Project File")
            dpg.add_separator()
            dpg.add_menu_item(label="Import new Feature")
            dpg.add_separator()
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Save As...")
            dpg.add_separator()
            dpg.add_menu_item(label="Preferences")
            dpg.add_menu_item(label="Exit", callback=cb.callback_exit_viewport)
        with dpg.menu(label="Project"):
            dpg.add_menu_item(label="Project Settings")
        with dpg.menu(label="Build"):
            dpg.add_menu_item(label="Update build dependencies", callback=cb.callback_install_build_deps)
            dpg.add_separator()
            dpg.add_menu_item(label="Build Debug")
            dpg.add_menu_item(label="Build Release")
        with dpg.menu(label="Terminal"):
            dpg.add_menu_item(label="Clear Termianl", callback=cb.callback_clearConsole)
        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="Support & Help")
            dpg.add_separator()
            dpg.add_menu_item(label="See current version")
            dpg.add_menu_item(label="View License")
            dpg.add_menu_item(label="About")
        dpg.add_separator()
        dpg.add_text(var.APP_CURRENT_PROJECT, color=(255, 255, 255, 180))

    # actions menu
    with dpg.window(label="Actions"
                    , width=210
                    , height=742
                    , no_close=True
                    , no_resize=True
                    , no_move=True
                    , no_collapse=True):
        dpg.add_text("-- OUTPUT --")
        dpg.add_text("Print Text to console")
        dpg.add_same_line()
        dpg.add_button(label="Add", callback=add_to_actionlist, user_data="_print")
        dpg.add_text("-- INPUT --")
    
    # console window
    with dpg.window(label="Console Log"
                    , width=790
                    , height=161
                    , no_close=True
                    , no_resize=True
                    , no_move=True
                    , no_collapse=True
                    , pos=(210, 600)
                    , tag="console"
                    , horizontal_scrollbar=True) as id._console_win:        
        pass
    
    # project viewer
    with dpg.window(label="Project"
                    , width=790
                    , height=581
                    , no_close=True
                    , no_resize=True
                    , no_move=True
                    , no_collapse=True
                    , pos=(210, 0)):
        pass

# Add text to the console
def add_to_console():
    dpg.delete_item("console", children_only=True)
    for message in CONSOLE_BUFFER:
        if message.startswith("ok_"):
            message = message.removeprefix("ok_")
            dpg.add_text("[  OK  ] " + message, parent="console")
        elif message.startswith("status_"):
            message = message.removeprefix("status_")
            dpg.add_text(":: " + message, parent="console")
        elif message.startswith("error_"):
            message = message.removeprefix("error_")
            dpg.add_text("[FAILED] " + message, parent="console")
        elif message.startswith("note_"):
            message = message.removeprefix("note_")
            dpg.add_text("[ NOTE ] " + message, parent="console")
        else:
            # buffertext in gray with no string prefix for specification (terminal stdout)
            dpg.add_text(message, parent="console", color=(255, 255, 255, 180))
    