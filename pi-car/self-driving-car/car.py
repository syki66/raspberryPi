import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk

def initpins():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

#MOTOR CONTROL FUNCTIONS
def reverse(t):
    GPIO.output(8, False)
    GPIO.output(10, True)
    GPIO.output(11, True)
    GPIO.output(12, False)
    time.sleep(t)
    GPIO.cleanup()
def forward(t):
    GPIO.output(8, True)
    GPIO.output(10, False)
    GPIO.output(11, False)
    GPIO.output(12, True)
    time.sleep(t)
    GPIO.cleanup()

def left(t):
    GPIO.output(10, True)
    GPIO.output(8, False)
    GPIO.output(12, True)
    GPIO.output(11, False)
    time.sleep(t)
    GPIO.cleanup()

def right(t):
    GPIO.output(10, False)
    GPIO.output(8, True)
    GPIO.output(12, False)
    GPIO.output(11, True)
    time.sleep(t)
    GPIO.cleanup()

def key_input(event):
    initpins()
    print 'Key:', event.char
    key_press = event.char
    sleep_time =0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        left(sleep_time)
    elif key_press.lower() == 'd':
        right(sleep_time)


command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
