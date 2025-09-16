import csv


def update_csv_column(csv_file, new_column):

    with open(csv_file, newline="", encoding="utf-8") as read_file:
        reader = csv.reader(read_file)
        rows = list(reader)

    if rows:
        rows[0].append(new_column)

    for idx in range(1, len(rows)):
        if len(rows) > 1:
            rows[idx].append(rows[idx][1])
        else:
            rows[idx].append("")

    with open(csv_file, "w", encoding="utf-8") as write_to:
        writer = csv.writer(write_to)
        writer.writerows(rows)


def run_csv_updater():
    update_csv_column("htmltexts.csv", "generalNewColumn")
    print("Program Finished")


def remove_column_from_csv(file_name, column_name):
    with open(file_name, newline="", encoding="utf-8") as read_file:
        reader = csv.reader(read_file)
        rows = list(reader)

    if not rows:
        print("No Such Column")
        return

    try:
        col_index = rows[0].index(column_name)
    except ValueError:
        print(f"Column |{column_name}| not Found")
        return

    for row in rows:
        if len(row) > col_index:
            del row[col_index]

    with open(file_name, "w", encoding="utf-8") as write_to:
        writer = csv.writer(write_to)
        writer.writerows(rows)


def run_remove_column():
    remove_column_from_csv("htmltexts.csv", "generalNewColumn")


# run_csv_updater()
run_remove_column()
