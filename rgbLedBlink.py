import .RgbLedGPIO
import time
import RPi.GPIO as GPIO
import sys

try:
	led = RgbLed(18, 23, 24)
	led.changeColour(100,100,100)
	led.toggle()
	time.sleep(3)
	led.toggle()
	time.sleep(1)
	led.toggle()
	time.sleep(2)
	led.changeColour(0,100,0)
	time.sleep(2)
	led.changeColour(0,0,100)
	time.sleep(2)
	led.changeColour(100,0,0)
	time.sleep(2)
	led.toggle()
	print 'success!!!'
except KeyboardInterrupt:
	print 'koniec'
except Exception, e:
	print "exc: %s" % e
finally:
	GPIO.cleanup()

