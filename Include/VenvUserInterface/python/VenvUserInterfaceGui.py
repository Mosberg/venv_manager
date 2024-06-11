import os
import subprocess
import tkinter as tk
from tkinter import filedialog

class VirtualEnvironmentManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual Environment Manager")
        self.master.geometry("850x600")

        self.create_input_fields()
        self.create_buttons()

    def create_input_fields(self):
        self.env_dir_entry = self.labels(
            "Environment Directory:", 0, 40
        )
        tk.Button(self.master, text="Browse", command=self.choose_venv_location).grid(row=0, column=2, padx=5, pady=5)

        self.env_name_entry = self.labels(
            "Environment Name:", 1, 20
        )
        # Create dropdown frame
        dropdown_frame = tk.Frame(self.master)
        dropdown_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        tk.Label(dropdown_frame, text="None/Symlinks/Copies:").grid(row=0, column=0, padx=5, pady=5)
        self.symlinks_var = tk.IntVar()
        tk.Radiobutton(dropdown_frame, text="None", variable=self.symlinks_var, value=0).grid(row=0, column=1, padx=5, pady=5)
        tk.Radiobutton(dropdown_frame, text="Symlinks", variable=self.symlinks_var, value=1).grid(row=0, column=2, padx=5, pady=5)
        tk.Radiobutton(dropdown_frame, text="Copies", variable=self.symlinks_var, value=2).grid(row=0, column=3, padx=5, pady=5)
        tk.Label(dropdown_frame, text="--symlinks: Try to use symlinks rather than copies, when symlinks are not the default for the platform.").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(dropdown_frame, text="--copies: Try to use copies rather than symlinks, even when symlinks are the default for the platform.").grid(row=2, column=0, padx=5, pady=5)


        # Create checkbox frame
        checkbox_frame = tk.Frame(self.master)
        checkbox_frame.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        self.system_site_packages_var = (
            self.check_buttons(
                checkbox_frame,
                "Include System Site-Packages",
                0,
                "Give the virtual environment access to the system site-packages",
            )
        )
        self.upgrade_deps_var = self.check_buttons(
            checkbox_frame,
            "Upgrade Core Dependencies",
            1,
            "Upgrade core dependencies (pip) to the latest version in PyPI",
        )
        self.upgrade_var = self.check_buttons(
            checkbox_frame,
            "Upgrade Environment Directory",
            2,
            "Upgrade the environment directory to use this version of Python, assuming Python has been upgraded in-place.",
        )
        self.without_pip_var = self.check_buttons(
            checkbox_frame,
            "Skip Installing/Upgrading Pip",
            3,
            "Skips installing or upgrading pip in the virtual environment (pip is bootstrapped by default)",
        )
        self.clear_var = self.check_buttons(
            checkbox_frame,
            "Clear Environment Directory",
            4,
            "Delete the contents of the environment directory if it already exists, before environment creation.",
        )

    def labels(self, text, row, width):
        # Create input fields and labels
        tk.Label(self.master, text=text).grid(row=row, column=0, padx=5, pady=5)
        result = tk.Entry(self.master, width=width)
        result.grid(row=row, column=1, padx=5, pady=5)
        return result

    def check_buttons(self, checkbox_frame, text, row, arg3):
        result = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text=text, variable=result).grid(
            row=row, column=0, padx=5, pady=5
        )
        tk.Label(checkbox_frame, text=arg3).grid(row=row, column=1, padx=5, pady=5)

        return result

    def create_buttons(self):
        tk.Button(self.master, text="Create Virtual Environment", command=self.create_venv).grid(row=4, column=0, columnspan=4, padx=5, pady=5)
        tk.Button(self.master, text="Activate Virtual Environment", command=self.activate_venv).grid(row=5, column=0, columnspan=4, padx=5, pady=5)
        tk.Button(self.master, text="Deactivate Virtual Environment", command=self.deactivate_venv).grid(row=6, column=0, columnspan=4, padx=5, pady=5)
        tk.Button(self.master, text="Remove Virtual Environment", command=self.remove_venv).grid(row=7, column=0, columnspan=4, padx=5, pady=5)

    def choose_venv_location(self):
        self.env_dir_entry.delete(0, tk.END)
        self.env_dir_entry.insert(0, filedialog.askdirectory())

    def create_venv(self):
        env_dir = self.env_dir_entry.get()
        env_name = self.env_name_entry.get()
        self.symlinks_var.get()
        system_site_packages = self.system_site_packages_var.get()
        upgrade= self.upgrade_var.get()
        self.upgrade_deps_var.get()
        without_pip = self.without_pip_var.get()
        clear = self.clear_var.get()

        if not env_dir or not env_name:
            print("Please fill in all fields")
            return

        if not os.path.exists(env_dir):
            os.makedirs(env_dir)

        venv_path = os.path.join(env_dir, env_name)
        if os.path.exists(venv_path):
            print("Virtual environment already exists")
            return

        command = f"python -m venv {'--system-site-packages' if system_site_packages else ''} {'--clear' if clear else ''} {'--upgrade' if upgrade else ''} {'--without-pip' if without_pip else ''} {venv_path}"
        subprocess.run(command, shell=True)

    def activate_venv(self):
        env_dir = self.env_dir_entry.get()
        env_name = self.env_name_entry.get()

        if not env_dir or not env_name:
            print("Please fill in all fields")
            return

        venv_path = os.path.join(env_dir, env_name)
        if not os.path.exists(venv_path):
            print("Virtual environment does not exist")
            return

        command = f"source {venv_path}/bin/activate"
        subprocess.run(command, shell=True)

    def deactivate_venv(self):
        command = "deactivate"
        subprocess.run(command, shell=True)

    def remove_venv(self):
        env_dir = self.env_dir_entry.get()
        env_name = self.env_name_entry.get()

        if not env_dir or not env_name:
            print("Please fill in all fields")
            return

        venv_path = os.path.join(env_dir, env_name)
        if not os.path.exists(venv_path):
            print("Virtual environment does not exist")
            return

        command = f"rm -rf {venv_path}"
        subprocess.run(command, shell=True)

root = tk.Tk()
venv_ui = VirtualEnvironmentManager(root)
root.mainloop()