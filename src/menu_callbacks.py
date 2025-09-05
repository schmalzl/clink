from src.install_deps import install_build_dependencies
import src.gui as gui

def callback_install_build_deps():
    install_build_dependencies()


def callback_exit_viewport():
    exit()


def callback_clearConsole():
    gui.CONSOLE_BUFFER = []

def callbackOpenProject(projectDirectory):
    pass