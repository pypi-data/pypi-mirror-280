
import sys
import subprocess
import argparse

from pyDendron import pyDendron_panel
#from pyDendron import pyDendron_import

try:
    parser = argparse.ArgumentParser(description="pydenron: A dendrochronology tool for tree-ring data analysis.")
    parser.add_argument('--www', action='store_true', help='A flag to enable www mode')
    parser.add_argument('--importdata', action='store_true', help='A flag to enable www mode')


    args = parser.parse_args()
    #page = pyDendron_import.__file__ if args.importdata else pyDendron_panel.__file__
    page = pyDendron_panel.__file__
    
    if args.www:
        subprocess.run([
            sys.executable, "-m", "panel", "serve", "--keep-alive", "0", "--show", "--autoreload", page, "--args", "--www"])
    else:
        subprocess.run([
            sys.executable, "-m", "panel", "serve", "--keep-alive", "0", "--show", "--autoreload", page])
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

