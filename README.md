<p align="center">
  <img src="https://raw.githubusercontent.com/faheel/desktop-entry-creator/master/desktop_entry_creator/res/icon.png" alt="Logo" width="128" height="128">
</p>
<h1 align="center">Desktop entry creator</h1>

[![PyPI][pypi-version-shield]][pypi-link]
[![License][license-shield]](LICENSE)

A user-friendly GUI for creating desktop entries for installed applications on Linux.

<p align="center">
  <img src="https://raw.githubusercontent.com/faheel/desktop-entry-creator/master/screenshot.png" alt="Screenshot">
</p>

## Installation

1. Install the required system packages:
   * Fedora and RHEL based distros:
     ```bash
     sudo dnf install python3-devel cairo cairo-devel python3-cairo gobject-introspection gobject-introspection-devel cairo-gobject cairo-gobject-devel
     ```
   * Ubuntu and Debian based distros:
     ```bash
     sudo apt install python3-dev libcairo2 libcairo-dev python3-cairo libgirepository-1.0-1 libgirepository1.0-dev libcairo-gobject2
     ```

2. Install using pip:
   ```bash
   pip install desktop-entry-creator
   ```

## Development

1. Install the required system packages mentioned in the installation section.
   * Also install pipenv
     ```bash
     sudo apt install pipenv
     ``` 
2. Set up a Python 3 virtual environment using [Pipenv][pipenv]:
   ```bash
   pipenv --three
   ```
3. Activate the virtual environment and install the dependencies:
   ```bash
   pipenv shell
   pipenv install --dev
   ```
4. Run `app.py` located under the `desktop_entry_creator` directory to launch the GUI:
   ```bash
   ./desktop_entry_creator/app.py
   ```

## License

This project is licensed under the terms of the [GPL v3 license](LICENSE).


[pypi-version-shield]: https://img.shields.io/pypi/v/desktop-entry-creator.svg?style=for-the-badge
[pypi-link]: https://pypi.org/project/desktop-entry-creator
[license-shield]: https://img.shields.io/github/license/faheel/desktop-entry-creator.svg?style=for-the-badge
[pipenv]: https://github.com/pypa/pipenv
