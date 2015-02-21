import RPi.GPIO as GPIO

class rgbLed:
	def __init__(self, rGPIO, gGPIO, bGPIO):
		self._redPin = rGPIO
		self._greenPin = gGPIO
		self._bluePin = bGPIO
	
		
