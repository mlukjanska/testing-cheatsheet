# Script to compare list of csv files row by rown in given folders - the differences are printed into console

import csv
import os

#List of csv files to compare in the respective folders
csvFiles = [
    'file1.csv',
    'file2.csv'
]

folder1 = 'old_folder_name'
folder2 = 'old_folder_name'

for csvFile in csvFiles:
    oldCsv = 'full_path_to_folder' + folder1 + '/' + csvFile
    newCsv = 'full_path_to_folder' + folder2 + '/' + csvFile

    if os.stat(oldCsv).st_size == 0:
        print('\n-----------------------------------------') 
        print('File is EMPTY: ' + oldCsv)
        continue

    if os.stat(newCsv).st_size == 0:
        print('\n-----------------------------------------\n') 
        print('File is EMPTY: ' + newCsv)
        continue

    with open(oldCsv, 'r') as f1:
        reader = csv.reader(f1)
        f1header = next(reader)  # gets the first (header) line
        f1row1 = next(reader)  # gets the next line

    with open(newCsv, 'r') as f2:
        reader = csv.reader(f2)
        f2header = next(reader) 
        f2row1 = next(reader) 

    print('\n-----------------------------------------') 
    if f1row1 != f2row1: 
        print('\nDIFFERENCES FOUND in: ' + csvFile + '\n')
        for index, column in enumerate(f1row1, start=0):
             if f1row1[index] != f2row1[index]:
                print(f1header[index] + ' ' + ' Old value: .' + f1row1[index] + '.  New value: .' + f2row1[index] + '. (' + f2header[index] + ')')
        print('\n')

    if f1row1 == f2row1: 
        print('No differences found in: ' + csvFile)