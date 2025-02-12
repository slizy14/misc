from openpyxl import Workbook

data = [
    ["apfel", 1.2, 10],
    ["birne", 1.4, 15],
    ["kirsche", 2.5, 7]
]

def write_to_csv(data, file_name="export.csv"):
    with open(file_name, "w") as file:
        for line in data:
            file.write(f"{line[0]};{line[1]};{line[2]}\n")

def write_to_excel(data, file_name="export.xlsx", sheet_title="data"):
    wb = Workbook()
    sheet = wb.active
    sheet.title = sheet_title

    for idx, line in enumerate(data, 1):
        line.append(f"=B{idx}*C{idx}")
        sheet.append(line)
    
    sheet.cell(4, 4, f"=sum(D1:D{idx})")
    wb.save(file_name)


write_to_csv(data)
write_to_excel(data)