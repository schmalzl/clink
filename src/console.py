import dearpygui.dearpygui as dpg # type: ignore

CONSOLE_BUFFER = []

def add_to_console(message):
    CONSOLE_BUFFER.append(message)