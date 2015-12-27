import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servoPIN=11
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN,50)
pwm.start(8)

for i in range(0,45):
	DC=1./18.*(i*4)+3
	pwm.ChangeDutyCycle(DC)
	time.sleep(.05)
for i in range(45,0,-1):
	DC=1./18.*(i*4)+3
	pwm.ChangeDutyCycle(DC)
	time.sleep(.05)

pwm.stop()
GPIO.cleanup()

