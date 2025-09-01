# clink

### Overview
This project is a bloat-free graphical user interface for building command-line applications. 
It allows anyone to design, configure, and export fully functional CLI tools without needing to manually write boilerplate code. 
The generated applications are lightweight, portable, and customizable to fit a wide variety of use cases.

The software is designed to empower both developers and non-developers to quickly create utilities, automation scripts, and workflows. 
It favors simplicity and productivity, focusing on ease of use rather than exhaustive feature sets found in complex development environments. 

This tool is particularly suited for prototyping utilities, building personal productivity scripts and teaching CLI fundamentals.

- Minimize time spent writing repetitive boilerplate.
- Minimize setup and configuration.
- Easy to use for both code-driven and no-code workflows.
- Portable and open-source, with minimal dependencies.
- Designed to create short-lived ad hoc tools as well as long-term reusable applications.
- Encourages experimentation, learning, and fast iteration.
- Lightweight runtime and efficient output.
- Community-driven and open to extension.

### How it works
Everything starts in the clink development window (UI). There, you will be able to add actions, if-statements, 
breaks and many other features to an action chain where everything will come together.
<br>
Once you build the application, clink will convert those actions from the chain into pure python code that can be exported
as either a python file for manual use in the terminal or directly to a self-contained executable for windows (.exe).

### Installation
You will find the newest Release of clink in the Releases tab of Github.
<br> Simply follow the instructions on the windows installer to install the main application.

Now, you will need to install Python. You can either get it using the Microsoft Store or download it online [here](https://www.python.org/downloads/).

You are almost ready to go. The only thing left is installing the build dependencies for clink. To do so, open clink studio and install the dependencies.
```
Build > Configuration > Install Build dependencies
```
clink will then run a installation script that installs every dependency it needs to be able to build all features into real code using pip.

### Getting started

### Usage

### Demo

### Documentation

### Releases & Changelogs

### Cross-Platform Support
Even though I will probably add full cross-platform support in the future, clink is mainly developed for windows 
users and based on the Windows commandline for system operations.
<br>
There are still many features that dont rely on operating system specific operations and are purely executed using python. This means
that if you can live without some functions, feel free to port this project to Mac and Linux Systems.

If you have any questions or ideas on improving cross-platform development, please tell me in the [Issues](https://github.com/schmalzl/clink/issues) Tab of Github
using the **enhancement** label.

### Gallery
*This project is still in active development so gallery pictures will be coming soon.*

### Support & FAQ
See [changelog.txt](./docs/changelog.txt) for detailed updates on this project.
<br> See [docs.md](./docs/docs.md) for a detailed feature documentation and starting guide.

For further support, feel free to open a new Topic in the [Issues](https://github.com/schmalzl/clink/issues) section of Github.

### Credits
Developed by Kian Schmalzl and inspired by many talented people of the coding community.

clink uses [Dear PyGui](https://github.com/hoffstadt/DearPyGui) by [hoffstadt](https://github.com/hoffstadt).
<br> Embeds [ProggyClean.ttf](https://www.dafont.com/proggy-clean.font) by Tristan Grimmer as a default UI font.

### License
clink is licensed under the MIT License. See [LICENSE.txt](./LICENSE.txt) for more information.