import csv

# входен и изходен файл
input_file = "htmltexts.csv"
output_file = "output.csv"

# новото име на колоната
new_column_name = "Copy_of_Col1"

with open(input_file, newline="", encoding="utf-8") as infile, \
        open(output_file, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # четем първия ред (заглавията)
    headers = next(reader)
    headers.append(new_column_name)
    writer.writerow(headers)

    # за всеки ред добавяме стойността от колоната на позиция 1
    for row in reader:
        if len(row) > 1:  # проверка дали съществува колона 1
            row.append(row[1])
        else:
            row.append("")  # ако няма, добавяме празно
        writer.writerow(row)

print(f"Новият CSV файл е записан като {output_file}")