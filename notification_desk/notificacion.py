import time
from datetime import datetime
from winotify import Notification,audio

while True:
    current_time=datetime.now()

    current_hour=current_time.strftime("%H:%M:%S")
    print(current_hour)

    time.sleep(1)

    if current_hour == "09:53:00":
        
        beginning=Notification(app_id="padrelson script",
        title="Notificacion",
        msg="Hora de Almorzar",
        duration="long",
        icon=r"C:/Users/Samuel/Documents/PROGRAMACION/APIS/notification_desk/lunch.jpg")

        beginning.set_audio(audio.Reminder,loop=True)
        beginning.show()
    