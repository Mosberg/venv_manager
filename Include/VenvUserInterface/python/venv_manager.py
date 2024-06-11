import tkinter as tk
from tkinter import messagebox
import sys
import subprocess
import os
import shutil
from colorama import Fore, Style
import argparse

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

# Create checkbox frame
        checkbox_frame = tk.Frame(self.input_frame)
        checkbox_frame.pack(fill="x")

        self.system_site_packages_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Include System Site-Packages", variable=self.system_site_packages_var).grid(row=0, column=0, padx=5, pady=5)

        self.symlinks_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Use Symlinks", variable=self.symlinks_var).grid(row=0, column=1, padx=5, pady=5)

        self.copies_var = tk.IntVar()
        tk.Checkbutton(checkbox_frame, text="Use Copies", variable=self.copies_var).grid(row=0, column=2, padx=5, pady=5)

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

    def create_environment(self):
    # Get input values
        self = self.env_dir_entry.get()
        options = []
        if self.system_site_packages_var.get():
            options.append("--system-site-packages")
        if self.symlinks_var.get():
            options.append("--symlinks")
        elif self.copies_var.get():
            options.append("--copies")
        if self.clear_var.get():
            options.append("--clear")
        if self.upgrade_var.get():
            options.append("--upgrade")
        if self.without_pip_var.get():
            options.append("--without-pip")
        if self.prompt_entry.get():
            options.append(f"--prompt {self.prompt_entry.get()}")
        if self.upgrade_deps_var.get():
            options.append("--upgrade-deps")

        # Create virtual environment
        venv_cmd = [sys.executable, "-m", "venv", self]
        venv_cmd.extend(options)
        try:
            subprocess.run(venv_cmd, check=True)
            print(f"{Fore.GREEN}Virtual environment created successfully at: {self}{Style.RESET_ALL}")
            self.output_text.insert("end", f"Virtual environment created successfully at: {self}\n")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error creating virtual environment: {e}{Style.RESET_ALL}")
            self.output_text.insert("end", f"Error creating virtual environment: {e}\n")

    def activate_environment(self):
# Get input values
        env_dir = self.env_dir_entry.get()

# Function to activate a virtual environment
        activate_script = os.path.join(env_dir, "bin", "activate")
        if os.path.exists(activate_script):
            try:
                subprocess.run([activate_script], check=True)
                print(f"{Fore.GREEN}Virtual environment activated: {env_dir}{Style.RESET_ALL}")
                self.output_text.insert("end", f"Virtual environment activated: {env_dir}\n")
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Error activating virtual environment: {e}{Style.RESET_ALL}")
                self.output_text.insert("end", f"Error activating virtual environment: {e}\n")
        else:
            print(f"{Fore.RED}Activate script not found: {activate_script}{Style.RESET_ALL}")
            self.output_text.insert("end", f"Activate script not found: {activate_script}\n")

    def deactivate_environment(self):
# Get input values
        env_dir = self.env_dir_entry.get()

# Function to deactivate a virtual environment
        deactivate_script = os.path.join(env_dir, "bin", "deactivate")
        if os.path.exists(deactivate_script):
            try:
                subprocess.run([deactivate_script], check=True)
                print(f"{Fore.GREEN}Virtual environment deactivated: {env_dir}{Style.RESET_ALL}")
                self.output_text.insert("end", f"Virtual environment deactivated: {env_dir}\n")
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Error deactivating virtual environment: {e}{Style.RESET_ALL}")
                self.output_text.insert("end", f"Error deactivating virtual environment: {e}\n")
        else:
            print(f"{Fore.RED}Deactivate script not found: {deactivate_script}{Style.RESET_ALL}")
            self.output_text.insert("end", f"Deactivate script not found: {deactivate_script}\n")

    def remove_environment(self):
# Get input values
        env_dir = self.env_dir_entry.get()

# Function to remove a virtual environment
        if os.path.exists(env_dir):
            try:
                shutil.rmtree(env_dir)
                print(f"{Fore.GREEN}Virtual environment removed: {env_dir}{Style.RESET_ALL}")
                self.output_text.insert("end", f"Virtual environment removed: {env_dir}\n")
            except OSError as e:
                print(f"{Fore.RED}Error removing virtual environment: {e}{Style.RESET_ALL}")
                self.output_text.insert("end", f"Error removing virtual environment: {e}\n")
        else:
            print(f"{Fore.RED}Virtual environment not found: {env_dir}{Style.RESET_ALL}")
            self.output_text.insert("end", f"Virtual environment not found: {env_dir}\n")

# Function to visualize virtual environment creation
    def visualize_venv_creation(self):
        
        """Prints a simple visual representation of the virtual environment structure."""
        
        print("{Fore.CYAN}Visualizing virtual environment structure for: {self}{Style.RESET_ALL}")
        print("├── bin")
        print("│   └── python -1")
        print("├── include")
        print("│   └── python -2")
        print("├── lib")
        print("│   └── python -3")
        print("└── pyvenv.cfg")

# Main function
    def main(self):
        parser = argparse.ArgumentParser(description="Manage Python virtual environments.")
        parser.add_argument("self", nargs="+", help="Target directory for the environment.")
        parser.add_argument(
            "--system-site-packages",
            action="store_true",
            help="Include system site-packages in the virtual environment.",
        )
        parser.add_argument(
            "--symlinks",
            action="store_true",
            help="Use symlinks instead of copies (default on most platforms).",
        )
        parser.add_argument(
            "--copies",
            action="store_true",
            help="Use copies instead of symlinks (overrides default on most platforms).",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete the contents of the environment directory if it already exists.",
        )
        parser.add_argument(
            "--upgrade",
            action="store_true",
            help="Upgrade the environment directory to use the current Python version.",
        )
        parser.add_argument(
            "--without-pip",
            action="store_true",
            help="Skip installing or upgrading pip in the environment.",
        )
        parser.add_argument("--prompt", help="Set the environment prompt prefix.")
        parser.add_argument(
            "--upgrade-deps",
            action="store_true",
            help="Upgrade core dependencies (like pip) to the latest version on PyPI.",
        )
        args = parser.parse_args()

        # Options for the venv command
        options = []
        if args.system_site_packages:
            options.append("--system-site_packages")
        if args.symlinks:
            options.append("--symlinks")
        if args.copies:
            options.append("--copies")
        if args.clear:
            options.append("--clear")
        if args.upgrade:
            options.append("--upgrade")
        if args.without_pip:
            options.append("--without-pip")
        if args.prompt:
            options.append(f"--prompt {args.prompt}")
        if args.upgrade_deps:
            options.append("--upgrade-deps")

root = tk.Tk()
my_gui = VirtualEnvironmentManager(root)
root.mainloop()