import os
import src.gui as gui
import re
import src.shared as sh

def open_project(directory):
    # To-Do
    # Check if directory exists
    if os.path.isdir(directory):
        # Check if project_settings.config exists
        full_path = directory + "/project_settings.config"
        gui.CONSOLE_BUFFER.append("ok_Locating project-directory...")
        if os.path.exists(full_path):
            gui.CONSOLE_BUFFER.append("ok_Locating project_settings.config file...")
            # Read project name
            print(full_path)
            f = open(str(full_path), "r", encoding="utf-8")
            gui.CONSOLE_BUFFER.append("ok_Reading project configuration...")
            data = f.read()
            match = re.search(r"project_name=(.+)", data)
            if match:
                p_name = match.group(1)
                # set variables in shared.py
                sh.APP_CURRENT_PROJECT = p_name
                sh.APP_CURRENT_PROJECT_LOCATION = directory
                gui.CONSOLE_BUFFER.append("ok_Opening Project...")
                gui.CONSOLE_BUFFER.append("--- Task executed successfully ---")
            else:
                gui.CONSOLE_BUFFER.append("error_The project name cannot be located. Has your project_setting.config file been changed?")

        else:
            gui.CONSOLE_BUFFER.append("error_This project folder does not contain a valid project structure (missing: project_settings.config)")
    else:
        gui.CONSOLE_BUFFER.append("error_The given project folder location is invalid and cannot be located.")