import pip
import subprocess
import requests
import pkg_resources

def get_installed_version(package_name):
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None

def get_latest_version(package_name):
    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
    if response.status_code == 200:
        data = response.json()
        return data['info']['version']
    return None

def notify_user_if_update_available(package_name):
    installed_version = get_installed_version(package_name)
    latest_version = get_latest_version(package_name)

    if installed_version and latest_version:
        if installed_version != latest_version:
            print(f"Update available for {package_name}: {installed_version} -> {latest_version}. Use 'pip install --upgrade {package_name}' to update the package")
        else:
            print(f"{package_name} is up-to-date (version {installed_version}).")
    elif not installed_version:
        print(f"{package_name} is not installed.")
    else:
        print(f"Could not fetch the latest version for {package_name}.")
