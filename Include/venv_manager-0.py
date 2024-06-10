# venv_manager.py
import os
import sys
import shutil
import subprocess
import argparse
from colorama import Fore, Style

# Function to create a virtual environment
def create_venv(env_dir, options):
    """Creates a virtual environment in the specified directory."""
    venv_cmd = [sys.executable, "-m", "venv", env_dir]
    venv_cmd.extend(options)
    try:
        subprocess.run(venv_cmd, check=True)
        print(f"{Fore.GREEN}Virtual environment created successfully at: {env_dir}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error creating virtual environment: {e}{Style.RESET_ALL}")

# Function to activate a virtual environment
def activate_venv(env_dir):
    """Activates a virtual environment."""
    activate_script = os.path.join(env_dir, "bin", "activate")
    if os.path.exists(activate_script):
        try:
            subprocess.run([activate_script], check=True)
            print(f"{Fore.GREEN}Virtual environment activated: {env_dir}{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error activating virtual environment: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Activate script not found: {activate_script}{Style.RESET_ALL}")

# Function to deactivate a virtual environment
def deactivate_venv(env_dir):
    """Deactivates a virtual environment."""
    deactivate_script = os.path.join(env_dir, "bin", "deactivate")
    if os.path.exists(deactivate_script):
        try:
            subprocess.run([deactivate_script], check=True)
            print(f"{Fore.GREEN}Virtual environment deactivated: {env_dir}{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error deactivating virtual environment: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Deactivate script not found: {deactivate_script}{Style.RESET_ALL}")

# Function to remove a virtual environment
def remove_venv(env_dir):
    """Removes a virtual environment."""
    if os.path.exists(env_dir):
        try:
            shutil.rmtree(env_dir)
            print(f"{Fore.GREEN}Virtual environment removed: {env_dir}{Style.RESET_ALL}")
        except OSError as e:
            print(f"{Fore.RED}Error removing virtual environment: {e}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Virtual environment not found: {env_dir}{Style.RESET_ALL}")

# Function to visualize virtual environment creation
def visualize_venv_creation(env_dir):
    """Prints a simple visual representation of the virtual environment structure."""
    print(f"{Fore.CYAN}Visualizing virtual environment structure for: {env_dir}{Style.RESET_ALL}")
    print(f"├── bin")
    print(f"│   └── python")
    print(f"├── include")
    print(f"│   └── python")
    print(f"├── lib")
    print(f"│   └── python")
    print(f"└── pyvenv.cfg")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Manage Python virtual environments.")
    parser.add_argument("env_dir", nargs="+", help="Target directory for the environment.")
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

    # Create virtual environments
    for env_dir in args.env_dir:
        create_venv(env_dir, options)
        visualize_venv_creation(env_dir)

        # Example of activating and deactivating a virtual environment
        # Activate the environment
        activate_venv(env_dir)

        # ... Do something in the activated environment ...

        # Deactivate the environment
        deactivate_venv(env_dir)

        # Example of removing a virtual environment
        remove_venv(env_dir)

if __name__ == "__main__":
    main()