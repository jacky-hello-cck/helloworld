#import necessary modules
import csv

reader = csv.DictReader(open('/path/data.csv','rt'))
for raw in reader:
        print(raw)
