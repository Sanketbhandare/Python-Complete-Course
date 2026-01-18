import csv

header = ["filename", "status"]

with open("backup-report.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
print("CSV file got created with required headers")

backup_data = [
    ["app.log","Success"],
    ["db.log","Failed"],
    ["config.log","Success"]
]
with open("backup-report.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(backup_data)

print("Backup data appended to csv file.")
with open("backup-report.csv","r",newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)