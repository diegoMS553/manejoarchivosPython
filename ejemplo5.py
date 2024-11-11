import zipfile
with zipfile.ZipFile("file.zip", "w") as zip_file:
    zip_file.write("file.txt")

with zipfile.ZipFile("file.zip", "r") as zip_file:
    zip_file.extractall("destination_directory")
