# Import the time library to allow us to use the sleep function 
# Import the datetime module using import datetime module  
import time, datetime 
 # Import RPi.GPIO module   
import RPi.GPIO as GPIO 
#Import telepot python library  
import telepot  
from telepot.loop import MessageLoop 
#Declare and initialize variables to store the GPIO number on which we connect the 
relay 
LED = 26 
FAN = 19 
BULB = 13 
TUBELIGHT = 6 
#Store the current date and time in variable(now) 
now = datetime.datetime.now() 
#Set the BCM mode 
GPIO.setmode(GPIO.BCM) 
# Disable warnings 
GPIO.setwarnings(False) 
#LED 
#set the pin number (GPIO 26) to output 
GPIO.setup(MYLED, GPIO.OUT) 
#LED initially off 
GPIO.output(LED, 1)  
 
#FAN 
#set the pin number (GPIO 19) to output 
GPIO.setup(FAN, GPIO.OUT) 
#FAN initially off 
GPIO.output(FAN, 1)  
 
 #BULB 
#set the pin number (GPIO 13) to output 
GPIO.setup(BULB, GPIO.OUT) 
#BULB initially off 
GPIO.output(BULB, 1)  
 
#TUBELIGHT 
#set the pin number (GPIO 6) to output 
GPIO.setup(TUBELIGHT, GPIO.OUT)
#TUBELIGHT initially off 
GPIO.output(TUBELIGHT, 1)  
 
#define function (action) 
def action(msg): 
    chat_id = msg['chat']['id'] 
    command = msg['text'] 
print 'Received: %s' % command 
 
if 'on' in command: 
        message = "Turned on " 
 
if 'LED' in command: 
            message = message + "LED " 
            GPIO.output(LED, 0) 
 
if 'FAN' in command: 
            message = message + "FAN " 
            GPIO.output(FAN, 0) 
 
if 'BULB' in command: 
            message = message + "BULB " 
            GPIO.output(BULB, 0) 

if 'TUBELIGHT' in command: 
            message = message + "TUBELIGHT " 
            GPIO.output(TUBELIGHT, 0) 
 
if 'all' in command: 
            message = message + "all " 
            GPIO.output(LED, 0) 
            GPIO.output(FAN, 0) 
            GPIO.output(BULB, 0) 
            GPIO.output(TUBELIGHT, 0) 
 
message = message + "light(s)" 
telegram_bot.sendMessage (chat_id, message) 
        
if 'off' in command: 
        message = "Turned off " 
    
        if 'LED' in command: 
            message = message + "LED " 
            GPIO.output(LED, 1) 
        if 'FAN' in command: 
            message = message + "FAN " 
        GPIO.output(FAN, 1) 
 
if 'BULB' in command: 
            message = message + "BULB " 
            GPIO.output(BULB, 1) 
 
if 'TUBELIGHT' in command: 
            message = message + "TUBELIGHT " 
            GPIO.output(TUBELIGHT, 1) 
 
if 'all' in command: 
            message = message + "all " 
            GPIO.output(LED, 1) 
            GPIO.output(FAN, 1) 
            GPIO.output(BULB, 1) 
            GPIO.output(TUBELIGHT, 1) 
 
message = message + "light(s)" 
telegram_bot.sendMessage (chat_id, message)  
telegram_bot = telepot.Bot('6203061528:AAEDVWXCmQo4LT4iW0kIvJxdhF1DhNQltA') 
print (telegram_bot.getMe()) 
MessageLoop(telegram_bot, action).run_as_thread() 
print 'Code GPG Home automation is Up and Running....' 
while 1: 
time.sleep(10) 