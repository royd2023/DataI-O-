import csv

filename = 'data/ev_stations_v1.csv'

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
try:
    with open(filename, 'r', encoding='utf-8') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    # printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end=" ")
        print('\n')
except FileNotFoundError:
    print(f"File {filename} not found.")
except UnicodeDecodeError as e:
    print(f"Error decoding file {filename}: {e}")