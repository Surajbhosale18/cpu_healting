# creating automation for calculating free space
import shutil     # used for calculating free space
import psutil     # used for calculating cpu work

# checking how much free space available
def check_disk_use(disk):
    disk_used= shutil.disk_usage(disk)
    free_space = disk_used.free / disk_used.total * 100
    return free_space > 20

# checking cpu health
def check_cpu_usage():
    usage  = psutil.cpu_percent(1)
    return usage < 75

# if both conditions are false
if not check_disk_use("/") or not check_cpu_usage():
    print("your pc have some problem ")
# if both conditions are true
else:
    print("you pc,s health is good")