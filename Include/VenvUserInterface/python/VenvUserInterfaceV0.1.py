import tkinter as tk
from tkinter import messagebox
import sys
import subprocess
import os
import shutil
from colorama import Fore, Style
import argparse

class VenvUserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Venv Manager")

        # Create a new virtual environment
        self.create_venv_button = tk.Button(self.root, text="Create Venv", command=lambda: self.create_venv("myenv", "3.9"))
        self.create_venv_button.pack()

        # Activate the virtual environment
        self.activate_venv_button = tk.Button(self.root, text="Activate Venv", command=lambda: self.activate_venv("myenv"))
        self.activate_venv_button.pack()

        # Deactivate the virtual environment
        self.deactivate_venv_button = tk.Button(self.root, text="Deactivate Venv", command=self.deactivate_venv)
        self.deactivate_venv_button.pack()

        # Remove the virtual environment
        self.remove_venv_button = tk.Button(self.root, text="Remove Venv", command=lambda: self.remove_venv("myenv"))
        self.remove_venv_button.pack()

        self.root.mainloop()

    def create_venv(self, name, python_version):
        try:
            # Create a new virtual environment using the specified Python version
            subprocess.run(
                [sys.executable, "-m", "venv", name, f"--python={python_version}"]
            )
        except Exception as e:
            # Handle any exceptions that may occur - 1
            print(f"An error occurred: {e}")

    def activate_venv(self, name):
        try:
            # Activate the specified virtual environment
            if os.name == "posix":
                subprocess.run(["source", f"{name}/bin/activate"])
            elif os.name == "nt":
                subprocess.run([f"{name}\\Scripts\\activate"], shell=True)
        except FileNotFoundError:
            # Handle the case where the virtual environment does not exist
            print(f"Virtual environment '{name}' does not exist.")
        except Exception as e:
            # Handle any other exceptions that may occur - 2
            print(f"An error occurred: {e}")

    def deactivate_venv(self):
        try:
            # Deactivate the current virtual environment
            if os.name == "posix":
                subprocess.run(["deactivate"])
            elif os.name == "nt":
                subprocess.run(["deactivate"], shell=True)
        except Exception as e:
            # Handle any exceptions that may occur - 3
            print(f"An error occurred: {e}")

    def remove_venv(self, name):
        try:
            # Remove the specified virtual environment
            shutil.rmtree(name)
        except FileNotFoundError:
            # Handle the case where the virtual environment does not exist - 2
            print(f"Virtual environment '{name}' does not exist.")
        except Exception as e:
            # Handle any other exceptions that may occur - 3
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    ui = VenvUserInterface()