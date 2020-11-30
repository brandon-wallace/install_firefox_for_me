#!/usr/bin/env python3
'''
Install Firefox from a tar.bz2 archive.
Requirements: Python3.4+

'''

import os
import shutil
import tarfile
import argparse
from pathlib import Path
from datetime import datetime


def check_firefox_edition(tar_bz2_file):
    '''Verify Firefox Edition'''

    if 'b' in tar_bz2_file:
        print('This appears to be Firefox developer edition.')
    else:
        print('This appears to be Firefox quantum edition.')


now = datetime.today().strftime('-%Y-%m-%d')

parser = argparse.ArgumentParser(description='Install Firefox Quantum \
                                 or Developer Edition.')

parser.add_argument('--file', type=str, required=True,
                    help='Specify the firefox-*.tar.bz2 archive.')

parser.add_argument('--dest', default='/opt/', type=str,
                    help='Specify a destination directory.')

parser.add_argument('--dev', required=False, action='store_true',
                    help='Install Firefox Developer Edition.')

args = parser.parse_args()

# Input file with path.
pkg = args.file

# Full path and filename.
archive_with_path = Path(pkg)

# File without extentions.
archive = archive_with_path.name.rsplit('.', 2)[0]

# Set which folder to install to.
if args.dev:
    install_folder = args.dest + 'firefox-developer-edition'
    # check_firefox_edition(archive)
    print('Installing Firefox Developer Edition.')
    print('Please wait...')
else:
    install_folder = args.dest + 'firefox-quantum'
    # check_firefox_edition(archive)
    print('Installing Firefox Quantum Edition.')
    print('Please wait...')

# If the directory exists rename it.
if os.path.exists(install_folder):
    shutil.move(install_folder, install_folder + now)

# Move archive to destination.
shutil.move(pkg, args.dest)

# Change directory.
os.chdir(args.dest)

# Extract file from tar.bz2 file.
with tarfile.open(pkg, mode='r:bz2') as tar:
    tar.extractall('.')

# Set the correct permissions on folder.
os.chmod('firefox/', 0o755)

# Rename directory.
shutil.move('firefox/', 'firefox-quantum')

print('Firefox has been in installed to {}.'.format(install_folder))
