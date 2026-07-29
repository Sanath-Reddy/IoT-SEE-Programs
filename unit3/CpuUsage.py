import os
import psutil

# Get the average CPU load over the last 1, 5, and 15 minutes
load1, load5, load15 = psutil.getloadavg()

# Calculate CPU usage percentage
cpu_usage = (load15 / os.cpu_count()) * 100

print("The CPU usage is:", cpu_usage)

# Get the percentage of RAM currently in use
print("RAM memory % used:", psutil.virtual_memory()[2])

# Get the amount of RAM used (in GB)
print("RAM Used (GB):", psutil.virtual_memory()[3] / 1000000000)