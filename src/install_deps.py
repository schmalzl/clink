import os
import subprocess
import src.gui as gui

def install_build_dependencies():
    # This function reads deps.txt and loops through each package and installs it using pip
    gui.CONSOLE_BUFFER.append("[ STATUS ] Updating build dependencies...")
    gui.CONSOLE_BUFFER.append("[ NOTE ] Depending on you connection speed, this process can take some time.")

    current_dir = os.path.dirname(__file__)
    deps_path = os.path.join(current_dir, "deps", "deps.txt")
    file = open(deps_path, "r")
    content = file.read()
    deps_array_raw = [line for line in content.split('\n') if line]

    for i in deps_array_raw:
        gui.CONSOLE_BUFFER.append("[ STATUS ] Checking for an active " + i + " installation...")
        result = subprocess.run(["pip", "install", i], capture_output=True, text=True)
        # print to console
        gui.CONSOLE_BUFFER.append(result.stdout)
        gui.CONSOLE_BUFFER.append("[ OK ] Executed pip command to install " + i)