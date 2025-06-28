import time 
from playsound import playsound
print("Creating a timer...")
time.sleep(2)
print(" Please input a number for the following quick timers: ")
time.sleep(1)
print("  For 15 minutes timer type 1")
print("  For 30 minutes timer type 2")
print("  For 1 hour timer type 3")
print("  For a Study/Work timer type 4")
print(" For your own timer press any other number")

CLEAR = "\033[2J" #I have no idea how this works i copied it i know what it does but idk why it's written like this 
CLEAR_CONSTANTLY = "\033[H"

def timer(seconds):
    time_elapse = 0

    print(CLEAR)
    while time_elapse < seconds:
        time.sleep(1) 
        time_elapse += 1 

        time_left = seconds - time_elapse 
        #what a mess it took me a while to understand this 
        hours_left = time_left // 3600
        remains = time_left % 3600 
        minutes_left = remains // 60 
        seconds_left = remains % 60 

        print(f"{CLEAR_CONSTANTLY}{hours_left:01d}:{minutes_left:02d}:{seconds_left:02d}")
    playsound("Majula.mp3")
#here i didn't know how to do the 2 degit thing and keep it around at all time the command was to add :02d

Timer = int(input('Select a timer: '))
if Timer == 1: 
    timer(15*60)
elif Timer == 2: 
    timer(30*60)
elif Timer == 3: 
    timer(1*3600)
elif Timer == 4:

    print ("The way this timer works,", "is every 20 minutes you take 5 minutes break,", " to avoid burnout and maximize focus.")
    time.sleep(10)
    cycles = 3
    for _ in range(cycles):

     timer(20*60)
     print("Time to take a break")
     time.sleep(5)
     timer(5*60)
else:
    
    hours = int(input("Hours? (eg 0 if you want only minutes timer): "))
    minutes = int (input("Minutes?(eg:1 for 1 minute): "))
    sec  = int(input("seconds? : "))
    sec_calc = hours*3600 + minutes *60 + sec
    timer(sec_calc)
