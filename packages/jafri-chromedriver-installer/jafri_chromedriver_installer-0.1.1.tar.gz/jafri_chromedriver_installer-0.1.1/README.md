# Jafri Chromedriver Installer

`jafri-chromedriver-installer` is a Python package that automatically updates the Chromedriver to match the installed Chrome version on your system. This package ensures that your Selenium tests run smoothly by always having the correct version of Chromedriver.

## Features

- Automatically detects the installed Chrome version on macOS and Windows.
- Downloads and extracts the matching Chromedriver version.
- Replaces the existing Chromedriver if the versions do not match.
- Easy to use via a simple command-line interface.

## How to use it:

You can just add these lines in your code before executing driver

<pre>
from jafri_chromedriver_installer import installer
installer.install_chromedriver()
</pre>

## Installation

You can install the package using `pip`:

```sh
pip3 install jafri-chromedriver-installer