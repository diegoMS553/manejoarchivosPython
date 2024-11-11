import csv
with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open("data.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])