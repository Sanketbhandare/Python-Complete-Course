# List comprehensions for efficiency

cpu_util = [30,60,85,87,99,95,91,45,48]
high_cpu = []
threshold = 85

for cpu in cpu_util:
    if cpu > threshold:
        high_cpu.append(cpu)

print("High CPU Utilization list is ",high_cpu)

cpu_util = [30,60,85,87,99,95,91,45,48]
high_cpu = [ cpu for cpu in cpu_util if cpu > 85 ]
print("High CPU Utilization list is ", high_cpu)