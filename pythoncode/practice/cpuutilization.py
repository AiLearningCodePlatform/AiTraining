import psutil

cpu_usage = psutil.cpu_percent(interval=1)

if cpu_usage > 80:
    print(" Warning: CPU utilization is high!", cpu_usage, "%")
else:
    print(" CPU utilization is normal.", cpu_usage, "%")
