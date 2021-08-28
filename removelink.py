import csv
import pandas as pd

with open('dataset0.csv', newline="") as f:
  reader = csv.reader(f)
  planet_data = list(reader)
dataset1 = []
for i in planet_data:
    print (len(i))
    i.pop(5)
    i.pop(5)
    i.pop(5)
    i.pop(5)
    i.pop(5)
    i.pop(5)
    dataset1.append(i)
dataset1.pop(0)

# convert array into dataframe
DF = pd.DataFrame(dataset1)
  
# save the dataframe as a csv file
DF.to_csv("data1.csv")