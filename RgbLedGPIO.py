import RPi.GPIO as GPIO

class RgbLed:
	def __init__(self, rGPIO, gGPIO, bGPIO):
		GPIO.setmode(GPIO.BCM)		
		GPIO.setup(rGPIO, GPIO.OUT)
		GPIO.setup(gGPIO, GPIO.OUT)
		GPIO.setup(bGPIO, GPIO.OUT)
		self._pwmRed = GPIO.PWM(rGPIO, 500)
		self._pwmGreen = GPIO.PWM(gGPIO, 500)
		self._pwmBlue = GPIO.PWM(bGPIO, 500)
		self._isOn = False
		self._red = 0
		self._green = 0
		self._blue = 0

	def changeColour(self, red, green, blue):
		if(red < 0 or red > 100):
			raise ValueError('Value of red should be between 0 and 100')
		if(green < 0 or green > 100):
			raise ValueError('Value of green should be between 0 and 100')
		if(blue < 0 or blue > 100):
			raise ValueError('Value of blue should be between 0 and 100')		
		self._red = red
		self._green = green
		self._blue = blue
		if self._isOn:
			self._pwmRed.ChangeDutyCycle(self._red)
			self._pwmGreen.ChangeDutyCycle(self._green)
			self._pwmBlue.ChangeDutyCycle(self._blue)

	def toggle(self):
		if self._isOn:
			self._pwmRed.stop()
			self._pwmGreen.stop()
			self._pwmBlue.stop()
			self._isOn = False
		else:
			self._pwmRed.start(self._red)
			self._pwmGreen.start(self._green)
			self._pwmBlue.start(self._blue)
			self._isOn = True
