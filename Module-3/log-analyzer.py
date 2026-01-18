# Project: Build a log analyzer that parses data and generates summaries using Python data structures.

logs = [
    "Error Disk Full",
    "Info Server Started",
    "Error CPU Overload",
    "Info Backup Completed"
]

error_count = 0

for log in logs:
    if "Error" in log:
        error_count +=1 

print("Total Errors in the logs are ",error_count)