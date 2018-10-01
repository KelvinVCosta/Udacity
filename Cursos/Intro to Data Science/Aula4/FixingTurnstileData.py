import csv


def fix_turnstile_data(filenames):
    for name in filenames:
        fout_name = 'updated_' + name
        fin = open(name, 'rb')
        fout = open(fout_name, 'wb')
        reader = csv.reader(fin, delimiter=',')
        writer = csv.writer(fout, delimiter=',')

        for row in reader:
            row_len = len(row)

            c1 = row[0]
            c2 = row[1]
            c3 = row[2]

            i = 3
            while i < row_len:
                updated = [c1, c2, c3, row[i], row[i + 1], row[i + 2], row[i + 3], row[i + 4]]
                writer.writerow(updated)
                i = i + 5

        fin.close()
        fout.close()