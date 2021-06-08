from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    time.sleep(1)
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is :",date)
        print(set_alarm_timer)
        print(now)
        print(now == set_alarm_timer)

        # check
        if now == set_alarm_timer:
            print("Time to Wake Up")
        winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
        
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


# create GUI alarm clock
clock = Tk()

clock.title('Alarm Clock by Imam')
clock.geometry("400x200")

time_format = Label(clock, text="Enter time in 24 hour format!", fg="red", bg="black", font="Arial").place(x=60, y=120)
addTime = Label(clock, text="Hour Min Sec", font=60).place(x=120)
setYourAlarm = Label(clock, text="When to wake you up?", fg="blue", relief="solid", font=("Helevetical",7,"bold")).place(x=0,y=29)

# the variable
hour = StringVar()
min = StringVar()
sec = StringVar()

# input time
hourTime = Entry(clock, textvariable=hour, bg="pink", width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="pink", width=15).place(x=160, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15).place(x=210, y=30)

# action to set alarm
submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=70)

# exec
clock.mainloop()