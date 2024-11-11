import openpyxl
workbook = openpyxl.load_workbook("file.xlsx")
sheet = workbook.active
print(sheet["A1"].value)

sheet["A1"] = "New value"
workbook.save("updated_file.xlsx")
