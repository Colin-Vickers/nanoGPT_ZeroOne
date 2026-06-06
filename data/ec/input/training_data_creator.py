# converts the IC_variants.csv file to a file full of tokens
# # the data is in the form:
# SEQUENCE_ID,STEP
# seq_0001,RECEIVE WAFER LOT
# seq_0001,LOT IDENTIFICATION
# seq_0001,INITIAL WAFER INSPECTION
# seq_0001,MEASURE SURFACE DEFECTS
# .. etcc

# note, we need to add start and end tokens to the beginning and end of the sequence

import csv
from tokenizer import convert_to_tokens

# start by opening the file and reading the data
# inital limit of 10 rows
counter = 0
sequence = []
with open('./data/tracks/industrial-infineon/training_data/IC_variants.csv', 'r') as file:
    reader = csv.reader(file)
    current_sequence = None
    for row in reader:
        # skip the first row
        if row[0] == 'SEQUENCE_ID':
            continue
    
        # if the row is empty, it means we are at the end of the file
        if len(row) == 0:
            sequence.append('(END)')
            break

        #if we are at the start of a new sequence, add the end and start tokens
        if current_sequence is None:
            current_sequence = row[0]
            sequence.append('(START)')
        elif row[0] != current_sequence:
            sequence.append('(END)')
            sequence.append('(START)')
            current_sequence = row[0]

        ic_command = row[1]
        sequence.append(ic_command)
        counter += 1
        # if counter > 1000:
        #     break
    
# add an (end) token to the end of the sequence if it is not already there
if sequence[-1] != '(END)':
    sequence.append('(END)')
print(sequence)

# save the sequence to a file
with open('ec_training_data.csv', 'w') as file:
    for token in sequence:
        file.write(token + ',')

#also save as a text file with one per line
with open('ec_training_data.txt', 'w') as file:
    for token in sequence:
        file.write(token + '\n')


# now we need to convert the current sequence to a sequence of tokens
tokens = convert_to_tokens(sequence)
print(tokens)

with open('ec_training_data_tokens.csv', 'w') as file:
    for token in tokens:
        file.write(str(token) + ',')

with open('ec_training_data_tokens.txt', 'w') as file:
    for token in tokens:
        file.write(str(token) + '\n')
        
print('read', counter, 'rows')
print('found', len(tokens), 'tokens')