# # we need to open ../data/tracks/industrial-infineon/training_data/IC_variants.csv, remove the initial sequence id and extract the alphabet
# # searching for unique tokens.
# # the data is in the form:
# SEQUENCE_ID,STEP
# seq_0001,RECEIVE WAFER LOT
# seq_0001,LOT IDENTIFICATION
# seq_0001,INITIAL WAFER INSPECTION
# seq_0001,MEASURE SURFACE DEFECTS
# .. etcc

import csv

# start by opening the file and reading the data
# inital limit of 10 rows
counter = 0
alphabet = []
with open('./data/tracks/industrial-infineon/training_data/IC_variants.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # skip the first row
        if row[0] == 'SEQUENCE_ID':
            continue
        # skip the seq_0001 - i.e. substring on the first comma in the second column
        if row[1].split(',')[0] not in alphabet:
            print(row[1].split(',')[0])
            alphabet.append(row[1].split(',')[0])
        counter += 1
        # if counter > 10:
        #     break

#double check the rows are unique
if len(alphabet) != len(set(alphabet)):
    print('duplicate tokens found')
    exit(1)

# save the alphabet to a file
with open('alphabet.txt', 'w') as file:
    for token in alphabet:
        file.write(token + '\n')

print('read', counter, 'rows')
print('found', len(alphabet), 'unique tokens')
