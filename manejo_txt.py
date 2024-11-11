with open("file.txt", "r") as file:
    content = file.read()

with open("file.txt", "a") as file:
    file.write("Additional text\n")
