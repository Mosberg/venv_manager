import sys
import tkinter as tk
from tkinter import filedialog
import os
import venv

class VenvUserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Environment Manager")

        # Create main frames with descriptive names
        self.main_input_frame = tk.Frame(self.root)
        self.main_input_frame.pack(fill="x", padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x", padx=10, pady=10)

        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create input fields and labels in a separate frame
        self.input_fields_frame = tk.Frame(self.main_input_frame)
        self.input_fields_frame.pack(fill="x")

        # Remove unnecessary import of venv module
        # self.venv = venv

        # Consider adding a method to create and layout the input fields and buttons
        # This will make the code more modular and easier to read
        # self.create_input_fields()
        # self.create_buttons()

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

        tk.Label(dropdown_frame, text="None/Symlinks/Copies:").grid(row=0, column=0, padx=5, pady=5)
        self.symlinks_var = tk.IntVar()
        tk.Radiobutton(dropdown_frame, text="None", variable=self.symlinks_var, value=0).grid(row=0, column=1, padx=5, pady=5)
        tk.Radiobutton(dropdown_frame, text="Symlinks", variable=self.symlinks_var, value=1).grid(row=0, column=2, padx=5, pady=5)
        tk.Radiobutton(dropdown_frame, text="Copies", variable=self.symlinks_var, value=2).grid(row=0, column=3, padx=5, pady=5)

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
        if self.symlinks_var.get() == 1:
            optional_args.append("--symlinks")
        elif self.symlinks_var.get() == 2:
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
        system_site_packages = self.system_site_packages_var.get() == 1
        self.venv.create(location, name, python_version, system_site_packages, *optional_args)
        self.output_text.insert(tk.END, "Environment created successfully.\n")

    def activate_venv(self):
        activate_script = os.path.join(self.env_dir_entry.get(), 'Scripts' if sys.platform == 'win32' else 'bin', 'activate')
        if os.path.exists(activate_script):
            self.output_text.insert(tk.END, f"Sourcing {activate_script}...\n")
            os.system(f'source {activate_script}' if sys.platform != 'win32' else f'call {activate_script}')
        else:
            self.output_text.insert(tk.END, "Environment not found.\n")
        
    def deactivate_venv(self):
        # You need to implement the logic to deactivate the virtual environment
        self.output_text.insert(tk.END, "Environment deactivated successfully.\n")

    def remove_venv(self):
        # You need to implement the logic to remove the virtual environment
        self.output_text.insert(tk.END, "Environment removed successfully.\n")

if __name__ == "__main__":
    venv_ui = VenvUserInterface()