import os
import sys
import json
import requests
import zipfile
import platform
import subprocess
from io import BytesIO


def get_chrome_version():
    try:
        if sys.platform == 'darwin':  # macOS
            result = subprocess.run(
                ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        elif sys.platform == 'win32':  # Windows
            result = subprocess.run(
                ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            version_line = [line for line in result.stdout.split('\n') if 'version' in line]
            if version_line:
                return version_line[0].split()[-1]
        else:
            return "Unsupported OS"
        return result.stdout.strip().split()[-1]
    except Exception as e:
        return f"Error: {str(e)}"


def get_system_platform():
    if sys.platform == 'darwin':  # macOS
        architecture = platform.machine()
        if architecture == "x86_64":
            return "mac-x64"
        elif architecture == "arm64":
            return "mac-arm64"
        else:
            return "Unknown architecture"
    elif sys.platform == 'win32':  # Windows
        architecture = platform.architecture()[0]
        if architecture == "32bit":
            return "win32"
        elif architecture == "64bit":
            return "win64"
        else:
            return "Unknown architecture"
    else:
        return "Unsupported OS"


def fetch_json():
    response = requests.get("https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json")
    response.raise_for_status()
    return response.json()


def find_matching_download(chrome_version, platform, json_data):
    download_url = None
    for item in json_data['versions']:
        if item['version'] == chrome_version:
            for download in item['downloads']['chromedriver']:
                if download['platform'] == platform:
                    download_url = download['url']
    if download_url is None:
        for item in json_data['versions']:
            inner_version = ".".join(item['version'].split(".")[:-1])
            inner_chrome_version = ".".join(chrome_version.split(".")[:-1])
            if inner_version == inner_chrome_version:
                for download in item['downloads']['chromedriver']:
                    if download['platform'] == platform:
                        download_url = download['url']

    return download_url


def download_and_extract_chromedriver(url, output_dir, chromedriver_file_name):
    response = requests.get(url)
    response.raise_for_status()

    with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
        for file in zip_file.namelist():
            if chromedriver_file_name in file and 'LICENSE' not in file:
                zip_file.extract(file, output_dir)
                os.rename(os.path.join(output_dir, file), os.path.join(output_dir, chromedriver_file_name))
                break


def get_chromedriver_version(chromedriver_file_name):
    try:
        result = subprocess.run(
            [chromedriver_file_name, '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip().split()[1]
    except Exception as e:
        return None


def install_chromedriver():
    chrome_version = get_chrome_version()
    platform = get_system_platform()

    chromedriver_file_name = ''
    if 'win' in platform:
        chromedriver_file_name = 'chromedriver.exe'
    elif 'mac' in platform:
        chromedriver_file_name = 'chromedriver'

    if "Error" in chrome_version or "Unsupported" in platform:
        print("Error detecting Chrome version or system platform.")
        return

    is_updated = False
    existing_chromedriver_version = get_chromedriver_version(chromedriver_file_name) if os.path.exists(chromedriver_file_name) else None
    if existing_chromedriver_version is not None:
        existing_chromedriver_version = ".".join(existing_chromedriver_version.split(".")[:-1])
        if existing_chromedriver_version in chrome_version:
            print("Chromedriver is updated.")
            is_updated = True

    if not is_updated:
        json_data = fetch_json()

        download_url = find_matching_download(chrome_version, platform, json_data)

        if download_url is None:
            print(f"No matching download found for Chrome version {chrome_version} on {platform}.")
        else:
            if existing_chromedriver_version:
                os.remove(chromedriver_file_name)

            download_and_extract_chromedriver(download_url, ".", chromedriver_file_name)
            print(f"{chromedriver_file_name} - 'v{chrome_version}' has been updated.")


