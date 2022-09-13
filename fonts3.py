import os
import sys
import pathlib

fonts_path = pathlib.PurePath(pathlib.Path.home().drive, os.sep, 'Windows', 'Fonts')
total_fonts = list(pathlib.Path(fonts_path).glob('*.fon'))
if not total_fonts:
    print("Fonts not available. Check path?")
    sys.exit()
print(total_fonts) 