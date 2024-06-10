# Python Virtual Environment Manager

This script provides a simple command-line interface for managing Python virtual environments. It leverages the built-in `venv` module and offers options for visualization, customization, and additional tools.

## Installation

1. Ensure you have Python 3.12 installed.
2. Clone this repository: `git clone https://github.com/your-username/venv-manager.git`
3. Navigate to the project directory: `cd venv-manager`
4. Install the dependencies: `pip install -r requirements.txt`

## Options

````text
--system-site-packages
```
: Include system site-packages in the virtual environment.


```
--symlinks
```
: Use symlinks instead of copies (default on most platforms).


```
--copies
```
: Use copies instead of symlinks (overrides default on most platforms).


```
--clear
```
: Delete the contents of the environment directory if it already exists.


```
--upgrade
```
: Upgrade the environment directory to use the current Python version.


```
--without-pip
```
: Skip installing or upgrading pip in the environment.


```
--prompt PROMPT
```
: Set the environment prompt prefix.


```
--upgrade-deps
```
: Upgrade core dependencies (like pip) to the latest version on PyPI.


## Usage

```bash
python venv_manager.py [OPTIONS] ENV_DIR [ENV_DIR ...]
```
````
