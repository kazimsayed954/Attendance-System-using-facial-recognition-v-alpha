import csv
row=['Id',"name"]
with open('StudentDetails.csv','a+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()