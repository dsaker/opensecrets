import csv

with open('cands90.txt', newline = '') as txtfile:
    reader = csv.reader(txtfile, quotechar='|')

    with open('cands90.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in reader:
            writer.writerow(row)