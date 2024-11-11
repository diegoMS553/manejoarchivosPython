import os
os.makedirs("new_directory", exist_ok=True)

from pathlib import Path
path = Path("new_directory/file.txt")
if path.exists():
    print("The file exists.")
