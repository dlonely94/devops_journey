import psutil
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cpu_usage = psutil.cpu_percent(interval=1)
ram_info = psutil.virtual_memory()
ram_used_gb = ram_info.used / (1024**3)

log_msg = (
    f"{now} | CPU: {cpu_usage}% | RAM Used: {ram_used_gb} GB ({ram_info.percent}%)\n"
)
print(log_msg.strip())
with open("monitor.log", "a") as f:
    f.write(log_msg)

if ram_info.percent > 80:
    alert_msg = f"{now} | WARNING: RAM usage is high ({ram_info.percent}%)\n"
    print(alert_msg.strip())
    with open("monitor.log", "a") as f:
        f.writable(alert_msg)
