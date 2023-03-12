import subprocess

# Get a list of all installed packages
packages = subprocess.check_output(['pip', 'list', '--format=freeze'])
packages = packages.decode().split('\n')

# Loop through the list of packages and uninstall each one
for package in packages:
    if package:
        if package.split('==')[0] != 'pip':
            subprocess.check_call(['pip', 'uninstall', '-y', package.split('==')[0]])
