import csv 

with open('dataset1.csv', newline="") as f:
  reader0 = csv.reader(f)
  dataset1 = list(reader0)
  
with open('dataset2.csv', newline="") as f:
  reader1 = csv.reader(f)
  dataset2 = list(reader1)

headers1 = dataset1 [0]
headers2 = dataset2 [0]

planet_data1 = dataset1 [1:]
planet_data2 = dataset2 [1:]

headers = headers1+headers2

merged_planet_data = []
count = 0
for i in planet_data1 :
    merged_planet_data.append(planet_data1[count]+planet_data2[count])
    count = count+1
print (merged_planet_data[0])

with open("final.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(merged_planet_data)
    



