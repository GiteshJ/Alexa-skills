import csv
myFile = open('3.csv', 'ab')
fname = "4.txt"
num_lines = 0
l=[]
with open(fname, 'r') as f:
    for line in f:
        if(len(line)>1):
            pos = line.find('.')
            pos = pos + 2
            num_lines += 1
            line = line[pos:]
            print(line)
            l.append(line)
print("Number of lines:")
print(num_lines)

writer = csv.writer(myFile)
for line in l: 
   writer.writerow([line])
'''
import csv
import random
import io
import codecs
import datetime
def givefact():
    l = []
    csvfile= io.open("3.csv", 'rb')
    reader = csv.reader(codecs.iterdecode(csvfile, 'utf-8',errors = 'ignore'))
    for row in reader:
        l.append(row)
    print(datetime.datetime.now())
    data = random.choice(l)[0]
    data = data.rstrip('\n')
    return data
if __name__ == '__main__':
    print(givefact())
'''
