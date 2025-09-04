import src.gui as gui
import os
import src.shared as var
import time

invalid_chars = r'\/:*?"<>|'

def has_invalid_chars(name: str) -> bool:
    return any(ch in invalid_chars for ch in name)

def create_new_project(project_name, project_directory):
    start = time.perf_counter()
    # Check if project Name is valid
    name_check = has_invalid_chars(project_name)
    # check if name is empty
    if project_name == "":
        gui.CONSOLE_BUFFER.append("error_Project name cannot be empty.")
        return None
    if name_check == True:
        gui.CONSOLE_BUFFER.append("error_Project name not allowed because it may contain forbidden characters.")
    else:
        gui.CONSOLE_BUFFER.append("ok_Checking project name...")
        # verify if project folder exists
        if os.path.isdir(project_directory):
            gui.CONSOLE_BUFFER.append("ok_Verifying project directory...")
            # create project folder
            os.makedirs(project_directory + "/" + project_name, exist_ok=True)
            # check if creation was successful
            full_path = project_directory + "/" + project_name
            if os.path.isdir(full_path):
                gui.CONSOLE_BUFFER.append("ok_Verifying project structure...")
                # add config file
                try:
                    with open(f"{full_path}/project_settings.config", "x") as f:
                        gui.CONSOLE_BUFFER.append("ok_Created project configuration file...")
                        # set values to that file
                        f.write(f"project_name={project_name}")
                        gui.CONSOLE_BUFFER.append("ok_Set default values to project_settings.config")
                except:
                    gui.CONSOLE_BUFFER.append("error_Failed to create and write project_settings.config. Does this file already exist?")

                gui.CONSOLE_BUFFER.append("ok_Project creation successful...")
                end = time.perf_counter()
                duration_ms = (end - start) * 1000
                gui.CONSOLE_BUFFER.append(f"--- Task executed successfully in {duration_ms:.3f} ms---")
                gui.CONSOLE_BUFFER.append(" ")
                gui.CONSOLE_BUFFER.append("status_Opening project...")
                # set current project to that project
                var.APP_CURRENT_PROJECT = project_name
                var.APP_CURRENT_PROJECT_LOCATION = full_path
                gui.CONSOLE_BUFFER.append("ok_Project opened...")
            else:
                gui.CONSOLE_BUFFER.append("error_Folder creation failed.")
        else:
            gui.CONSOLE_BUFFER.append("error_The given project directory does not exist.")


