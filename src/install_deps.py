# clink, v0.1.dev WIP
# (dependency installer and updater)

import os               # file operations
import subprocess       # terminal execution (pip)
import src.gui as gui   # console logging

def install_build_dependencies():
    # This function reads deps.txt and loops through each package and installs it using pip
    current_dir = os.path.dirname(__file__)
    deps_path = os.path.join(current_dir, "deps", "deps.txt")
    
    if os.path.isfile(deps_path):                                               # check if the deps.txt file is available
        gui.CONSOLE_BUFFER.append("ok_Verifying dependency list (deps.txt)")
        
        file = open(deps_path, "r")                                             # Open the file in read-mode and add all elements 
        content = file.read()                                                   # to an array.
        deps_array_raw = [line for line in content.split('\n') if line]
        gui.CONSOLE_BUFFER.append("ok_Reading packages...")
        gui.CONSOLE_BUFFER.append("status_Packages found: " + str(len(deps_array_raw)))
        
        gui.CONSOLE_BUFFER.append("")

        for i in deps_array_raw:                                                                # Loop through the array and install every package
            gui.CONSOLE_BUFFER.append("ok_Checking for an active " + i + " installation...")
            gui.CONSOLE_BUFFER.append("status_Downloading " + i)
            result = subprocess.run(["pip", "install", i], capture_output=True, text=True)
            # print to console
            gui.CONSOLE_BUFFER.append(result.stdout)
            gui.CONSOLE_BUFFER.append("ok_" + i + " installation command executed.")
        
        gui.CONSOLE_BUFFER.append("ok_" + str(len(deps_array_raw)) + " packages have been installed and updated.")
        gui.CONSOLE_BUFFER.append("--- Process complete ---")
    else:
        gui.CONSOLE_BUFFER.append("error_Verifying dependency list (deps.txt)")         # Throw file_not_found exception