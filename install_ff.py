#!/usr/bin/env python3
'''
Install Firefox from a tar.bz2 archive.
Requirements: Python3.4+

'''

import os
import sys
import shutil
import tarfile
import argparse
from pathlib import Path
from datetime import datetime


def check_firefox_edition(tar_bz2_file):
    '''Verify Firefox Edition'''

    if 'b' in tar_bz2_file:
        sys.exit('This appeares to be the \
                 developer edition. Use --dev.')


now = datetime.today().strftime('-%Y-%m-%d-%Hh%Mm%Ss')

parser = argparse.ArgumentParser(description='Install Firefox Quantum \
                                 or Developer Edition.')

parser.add_argument('--file', type=str, required=True,
                    help='Specify the firefox-*.tar.bz2 archive.')

parser.add_argument('--dest', default='/opt/', type=str,
                    help='Specify a destination directory.')

parser.add_argument('--dev', required=False, action='store_true',
                    help='Install Firefox Developer Edition.')

args = parser.parse_args()

if Path(args.file).is_file():
    # Input file with path.
    pkg = args.file
else:
    # Exit if file does not exist.
    sys.exit('File not found.')

# Full path and filename.
archive_with_path = Path(pkg)

# File without extentions.
archive = archive_with_path.name.rsplit('.', 2)[0]

# Set which folder to install to.
if args.dev:
    install_directory = 'firefox-developer-edition'
    install_path = args.dest + 'firefox-developer-edition'
    print('Installing Firefox Developer Edition.')
    print('Please wait...')
else:
    install_directory = 'firefox-quantum'
    install_path = args.dest + 'firefox-quantum'
    check_firefox_edition(archive)
    print('Installing Firefox Quantum Edition.')
    print('Please wait...')

# If the directory exists rename it.
if Path(install_path).is_dir():
    old_directory = Path(install_path)
    new_directory = install_path + now
    old_directory.rename(new_directory)

# Move archive to destination.
shutil.move(pkg, args.dest)

# Change directory.
os.chdir(args.dest)

# Extract file from tar.bz2 file.
with tarfile.open(pkg, mode='r:bz2') as tar:
    tar.extractall('.')

# Set the correct permissions on folders.
os.chmod('firefox/', 0o755)

root_dir = Path('firefox/')

subdirectories = [x for x in root_dir.iterdir() if x.is_dir()]

for j in subdirectories:
    os.chmod(j, 0o755)

# Rename directory.
shutil.move('firefox/', install_directory)

# Remove archive after installation is done.
bz2_file = Path(pkg)
bz2_file.unlink()

print('Firefox has been in installed to {}.'.format(install_path))
