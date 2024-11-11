with open("image.jpg", "rb") as binary_file:
    content = binary_file.read()

with open("copy_image.jpg", "wb") as binary_file:
    binary_file.write(content)
