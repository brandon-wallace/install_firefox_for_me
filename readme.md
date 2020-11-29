# Install Firefox For Me

# Install Firefox from a tar.bz2 archive.

## Requirements: Python3.4+


1. Download the latest firefox-*.tar.bz2 Quantum or Developer edition archive.


2. Make the file executable.
```
$ chmod +x install_ff.py

```

3. Run the script to install Firefox Quantum like this.
```
$ sudo ./install_ff.py --file firefox-83.0.tar.bz2

```
... or install Firefox Developer Edition with the **--dev** flag.

```
$ sudo ./install_ff.py --file firefox-84.0b5.tar.bz2 --dev

```

4. Create a desktop shortcut that points to /opt/firefox-quantum/firefox

...or /opt/firefox-developer-edition/firefox.
