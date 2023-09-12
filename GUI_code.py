from tkinter import*
import tkinter.font
from gpiozero import LED 
import RPi.GPIO
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)

##LED PINS
red_Led = LED(16)
blue_Led = LED(20)
green_Led = LED(21)
##GUI##
win=Tk()
win.title("LED Control")
myFont = tkinter.font.Font(family='Helveticq', size = 12, weight='bold')
##EVENT##
def RedLED():
    if red_Led.is_lit:
        red_Led.off()
        RedledButton["text"]= "Turn on Red LED"
    else:
        red_Led.on()
        RedledButton["text"]= "Turn off Red LED"
        blue_Led.off()
        BlueledButton["trext"]= "Turn on blue LED"
        green_Led.off()
        GreenledButton["text"] = "Turn on green LED"

def BlueLED():
    if blue_Led.is_lit:
        blue_Led.off()
        BlueledButton["text"]= "Turn on Blue LED"
    else:
        blue_Led.on()
        BlueledButton["text"]= "Turn off blue LED"
        blue_Led.off()
        RedledButton["trext"]= "Turn on red LED"
        green_Led.off()
        GreenledButton["text"] = "Turn on green LED"

def GreenLED():
    if green_Led.is_lit:
        green_Led.off()
        GreenledButton["text"]= "Turn on green LED"
    else:
        green_Led.on()
        GreenledButton["text"]= "Turn off green LED"
        blue_Led.off()
        BlueledButton["trext"]= "Turn on blue LED"
        red_Led.off()
        RedledButton["text"] = "Turn on red LED"
        
        
def close():
           
        RPi.GPIO.cleanup()
        win.destroy()

             
##WIDGETS##
RedledButton = Button(win, text='Turn led on Red LED', font=myFont, command=RedLED, bg='bisque2', height=1, width=24)
RedledButton.grid(row=0, column=1)
BlueledButton = Button(win, text='Turn led on Blue LED', font=myFont, command=BlueLED, bg='bisque2', height=1, width=24)
BlueledButton.grid(row=1, column=1)
GreenledButton = Button(win, text='Turn led on Green LED', font=myFont, command=GreenLED, bg='bisque2', height=1, width=24)
GreenledButton.grid(row=2, column=1)
ExistledButton = Button(win, text='EXIST', font=myFont, command=close, bg='red', height=1, width=6)
ExistledButton.grid(row=3, column=1)
win.mainloop()
