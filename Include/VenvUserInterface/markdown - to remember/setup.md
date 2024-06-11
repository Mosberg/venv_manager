# Project Venv User Interface

This is a simple user interface for managing Python virtual environments using the `venv` module.
It allows users to create, list, and delete virtual environments, as well as activate and deactivate them

## Class: `VenvUserInterface`

This class is responsible for handling user input and output for the Project Venv application.
It provides a command-line interface for users to interact with the application.

### __init__(self)

Initializes the `VenvUserInterface` object.
Sets up the command-line interface and defines the available commands.

### choose_venv_location(self)

Opens a file dialog for the user to choose a location for the new virtual environment.
Returns the chosen location as a string.

### choose_venv_name(self)

Asks the user to input a name for the new virtual environment.
Returns the chosen name as a string.

### choose_python_version(self)

Asks the user to choose a Python version to download and install.
Returns the chosen version as a string.

### choose_optional_args(self)

Asks the user if they want to include optional arguments (e.g., `--system-site-packages`).
Returns a boolean indicating whether to include optional arguments.

### create_venv(self)

Creates a new virtual environment with the chosen location, name, Python version, and optional arguments.
Calls the `create_venv` function from the `VenvManager` class.

### activate_venv(self)

Activates the virtual environment.
Calls the `activate_venv` function from the `VenvManager` class.

### deactivate_venv(self)

Deactivates the virtual environment.
Calls the `deactivate_venv` function from the `VenvManager` class.

### remove_venv(self)

Removes the virtual environment.
Calls the `remove_venv` function from the `VenvManager` class.

```python
import tkinter as tk
from tkinter import filedialog
import os
import venv_manager

class VenvUserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Environment Manager")
        self.venv_manager = venv_manager.VenvManager()

        # Create GUI elements
        self.location_label = tk.Label(self.root, text="Location:")
        self.location_label.pack()
        self.location_entry = tk.Entry(self.root, width=50)
        self.location_entry.pack()
