# Project Venv User Interface

## Class: VenvUserInterface

The `VenvUserInterface` class is responsible for managing user input and output for the Project Venv application. It provides a command-line interface for users to interact with the application.

### Method: __init__

This method initializes the `VenvUserInterface` object. It sets up the command-line interface and defines the available commands.

### Method: choose_venv_location

This method opens a file dialog for the user to select a location for the new virtual environment. It returns the chosen location as a string.

### Method: choose_venv_name

This method prompts the user to input a name for the new virtual environment. It returns the chosen name as a string.

### Method: choose_python_version

This method prompts the user to select a Python version to download and install. It returns the chosen version as a string.

### Method: choose_optional_args

This method asks the user if they want to include optional arguments (e.g., --system-site-packages). It returns a boolean indicating whether to include optional arguments.

### Method: create_venv

This method creates a new virtual environment with the chosen location, name, Python version, and optional arguments. It calls the `create_venv` function from the `VenvManager` class.

### Method: activate_venv

This method activates the virtual environment. It calls the `activate_venv` function from the `VenvManager` class.

### Method: deactivate_venv

This method deactivates the virtual environment. It calls the `deactivate_venv` function from the `VenvManager` class.

### Method: remove_venv

This method removes the virtual environment. It calls the `remove_venv` function from the `VenvManager` class.

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
```

The following methods have been implemented:

choose_location: Opens a file dialog for the user to choose a location for the new virtual environment.

choose_venv_name: Asks the user to input a name for the new virtual environment.

choose_python_version: Asks the user to choose a Python version to download and install.

choose_optional_args: Asks the user if they want to include optional arguments. The options are as follows:

Checkbox Input: --system-site-packages - Gives the virtual environment access to the system site-packages directory.

Dropdown Input: There are two options:

Option 1: --symlinks - Tries to use symlinks rather than copies, when symlinks are not the default for the platform.

Option 2: --copies - Tries to use copies rather than symlinks, even when symlinks are the default for the platform.

Checkbox Input: --clear - Deletes the contents of the environment directory if it already exists, before environment creation.

Checkbox Input: --upgrade - Upgrades the environment directory to use this version of Python, assuming Python has been upgraded in-place.

Checkbox Input: --without-pip - Skips installing or upgrading pip in the virtual environment (pip is bootstrapped by default).

Checkbox Input: --prompt PROMPT - Provides an alternative prompt prefix for this environment.

Checkbox Input: --upgrade-deps - Upgrades core dependencies (pip) to the latest version in PyPI.

create_venv: Creates a new virtual environment with the chosen location, name, Python version, and optional arguments.

activate_venv: Activates the virtual environment.

deactivate_venv: Deactivates the virtual environment.

remove_venv: Removes the virtual environment.

The GUI components for the above methods have also been implemented. The complete code for the GUI is as follows:

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

    # Create main frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill="x", padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x", padx=10, pady=10)

        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create input fields and labels
        input_fields_frame = tk.Frame(self.input_frame)
        input_fields_frame.pack(fill="x")

        tk.Label(input_fields_frame, text="Environment Directory:").grid(row=0, column=0, padx=5, pady=5)
        self.env_dir_entry = tk.Entry(input_fields_frame, width=40)
        self.env_dir_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(input_fields_frame, text="Browse", command=self.choose_venv_location).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(input_fields_frame, text="Environment Name:").grid(row=1, column=0, padx=5, pady=5)
        self.env_name_entry = tk.Entry(input_fields_frame, width=20)
        self.env_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_fields_frame, text="Python Version:").grid(row=2, column=0, padx=5, pady=5)
        self.python_version_entry = tk.Entry(input_fields_frame, width=20)
        self.python_version_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create dropdown frame
        dropdown_frame = tk.Frame(self.input_frame)
        dropdown_frame.pack(fill="x")

        tk.Label(dropdown_frame, text="Symlinks/Copies:").grid(row=0, column=0, padx=5, pady=5)
        self.symlinks_var = tk.IntVar()
        tk.Radiobutton(dropdown_frame, text="Symlinks", variable=self.symlinks_var, value=1).grid(row=0, column=1, padx=5, pady=5)
        tk.Radiobutton(dropdown_frame, text="Copies", variable=self.symlinks_var, value=0).grid(row=0, column=2, padx=5, pady=5)

        # Create checkbox frame
        checkbox_frame = tk.Frame(self.input_frame)
        checkbox_frame.pack(fill="x")

        self.system_site_packages_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Include System Site-Packages", variable=self.system_site_packages_var).grid(row=0, column=0, padx=5, pady=5)

        self.clear_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Clear Environment Directory", variable=self.clear_var).grid(row=1, column=0, padx=5, pady=5)

        self.upgrade_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Upgrade Environment Directory", variable=self.upgrade_var).grid(row=1, column=1, padx=5, pady=5)

        self.without_pip_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Skip Installing/Upgrading Pip", variable=self.without_pip_var).grid(row=1, column=2, padx=5, pady=5)

        self.upgrade_deps_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Upgrade Core Dependencies", variable=self.upgrade_deps_var).grid(row=2, column=0, padx=5, pady=5)

        # Create buttons
        tk.Button(self.button_frame, text="Create Environment", command=self.create_venv).pack(side="left", padx=5, pady=5)
        tk.Button(self.button_frame, text="Activate Environment", command=self.activate_venv).pack(side="left", padx=5, pady=5)
        tk.Button(self.button_frame, text="Deactivate Environment", command=self.deactivate_venv).pack(side="left", padx=5, pady=5)
        tk.Button(self.button_frame, text="Remove Environment", command=self.remove_venv).pack(side="left", padx=5, pady=5)

        # Create output text box
        tk.Label(self.output_frame, text="Environment Creation Log:").pack(fill="x", padx=5, pady=5)
        self.output_text = tk.Text(self.output_frame, width=80)
        self.output_text.pack(fill="both", expand=True, padx=5, pady=5)

        self.root.mainloop()

    def choose_venv_location(self):
        self.env_dir_entry.delete(0, tk.END)
        self.env_dir_entry.insert(0, filedialog.askdirectory())

    def choose_venv_name(self):
        return self.env_name_entry.get()

    def choose_python_version(self):
        return self.python_version_entry.get()

    def choose_optional_args(self):
        optional_args = []
        if self.system_site_packages_var.get():
            optional_args.append("--system-site-packages")
        if self.symlinks_var.get():
            optional_args.append("--symlinks")
        else:
            optional_args.append("--copies")
        if self.clear_var.get():
            optional_args.append("--clear")
        if self.upgrade_var.get():
            optional_args.append("--upgrade")
        if self.without_pip_var.get():
            optional_args.append("--without-pip")
        if self.upgrade_deps_var.get():
            optional_args.append("--upgrade-deps")
        return optional_args

    def create_venv(self):
        location = self.env_dir_entry.get()
        name = self.choose_venv_name()
        python_version = self.choose_python_version()
        optional_args = self.choose_optional_args()
        self.venv_manager.create_venv(location, name, python_version, optional_args)
        self.output_text.insert(tk.END, "Environment created successfully.\n")

    def activate_venv(self):
        self.venv_manager.activate_venv()
        self.output_text.insert(tk.END, "Environment activated successfully.\n")

    def deactivate_venv(self):
        self.venv_manager.deactivate_venv()
        self.output_text.insert(tk.END, "Environment deactivated successfully.\n")

    def remove_venv(self):
        self.venv_manager.remove_venv()
        self.output_text.insert(tk.END, "Environment removed successfully.\n")

if __name__ == "__main__":
    venv_ui = VenvUserInterface()
```

This script creates a GUI with the following features:

* Create a new virtual environment
*
* Activate the virtual environment
*
* Deactivate the virtual environment
*
* Remove the virtual environment
*

The script uses the `venv` module to create, activate, deactivate, and remove virtual environments

## Code Explanation

Here's a breakdown of the code:

### Importing Modules

The script starts by importing the necessary modules. `tkinter` is used to create the GUI,
`os` is used to interact with the operating system, and `venv` is used to
manage virtual environments.

### Class Definition

The `VenvUserInterface` class is defined. This class will contain all the methods and
attributes necessary to create the GUI and manage virtual environments.

### `__init__` Method

The `__init__` method is a special method in Python classes that is automatically
called when an object of the class is created. In this method, the GUI is created
using `tkinter`. The method initializes the following attributes:

* `root`: The main window of the GUI.
*
* `env_dir_entry`: A text entry field where the user can enter the directory
*
* `env_name_entry`: A text entry field where the user can enter the name of the
