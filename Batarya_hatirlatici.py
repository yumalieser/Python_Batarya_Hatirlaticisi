import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()
while True:
    percent = battery.percent
    notification.notify(
        title="Batarya Yüzdesi",
        message="%" + str(percent) + " batarya kaldı." ,
        timeout=7
    )
    time.sleep(60*60)
    continue