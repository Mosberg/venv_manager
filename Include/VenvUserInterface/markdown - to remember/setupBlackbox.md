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
```

choose_location: Opens a file dialog for the user to choose a location for the new virtual environment.

choose_venv_name: Asks the user to input a name for the new virtual environment.

choose_python_version: Asks the user to choose a Python version to download and install.

choose_optional_args: Asks the user if they want to include optional arguments (e.g., --system-site-packages).

create_venv: Creates a new virtual environment with the chosen location, name, Python version, and optional arguments.

activate_venv: Activates the virtual environment.

deactivate_venv: Deactivates the virtual environment.

remove_venv: Removes the virtual environment.

I have also implemented the GUI components for the above methods. Here is the complete code for the GUI:

```python
class VirtualEnvironmentManager:
    def __init__(self, master):
        self.master = master
        master.title("Python Virtual Environment Manager")

# Create main frames
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(fill="x", padx=10, pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(fill="x", padx=10, pady=10)

        self.output_frame = tk.Frame(master)
        self.output_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create input fields and labels
        input_fields_frame = tk.Frame(self.input_frame)
        input_fields_frame.pack(fill="x")

        tk.Label(input_fields_frame, text="Environment Directory:").grid(row=0, column=0, padx=5, pady=5)
        self.env_dir_entry = tk.Entry(input_fields_frame, width=40)
        self.env_dir_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_fields_frame, text="Prompt Prefix:").grid(row=1, column=0, padx=5, pady=5)
        self.prompt_entry = tk.Entry(input_fields_frame, width=20)
        self.prompt_entry.grid(row=1, column=1, padx=5, pady=5)

# Create dropdown frame
        dropdown_frame = tk.Frame(self.input_frame)
        dropdown_frame.pack(fill="x")

        self.symlinks_var = tk.IntVar()
        tk.dropdown(dropdown_frame, text="Use Symlinks", variable=self.symlinks_var).grid(row=0, column=1, padx=5, pady=5)

        self.copies_var = tk.IntVar()
        tk.dropdown(dropdown_frame, text="Use Copies", variable=self.copies_var).grid(row=0, column=2, padx=5, pady=5)

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
        tk.Button(self.button_frame, text="Create Environment", command=self.create_environment).pack(side="left", padx=5, pady=5)
        tk.Button(self.button_frame, text="Activate Environment", command=self.activate_environment).pack(side="left", padx=5, pady=5)
        tk.Button(self.button_frame, text="Deactivate Environment", command=self.deactivate_environment).pack(side="left", padx=5, pady=5)
        tk.Button(self.button_frame, text="Remove Environment", command=self.remove_environment).pack(side="left", padx=5, pady=5)

# Create output text box
        tk.Label(self.output_frame, text="Environment Creation Log:").pack(fill="x", padx=5, pady=5)
        self.output_text = tk.Text(self.output_frame, width=80)
        self.output_text.pack(fill="both", expand=True, padx=5, pady=5)

```
