import os
import subprocess

def install_build_dependencies():
    # This function reads deps.txt and loops through each package and installs it using pip
    current_dir = os.path.dirname(__file__)
    deps_path = os.path.join(current_dir, "deps", "deps.txt")
    file = open(deps_path, "r")
    content = file.read()
    deps_array_raw = [line for line in content.split('\n') if line]
    print(deps_array_raw)

    for i in deps_array_raw:
        result = subprocess.run(["pip", "install", i], capture_output=True, text=True)
        # print to console
        print(result.stdout)