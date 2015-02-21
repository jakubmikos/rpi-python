import RPi.GPIO as GPIO

class rgbLed:
	def __init__(self, rGPIO, gGPIO, bGPIO):
		GPIO.setmode(GPIO.BCM)
		
		GPIO.setup(rGPIO, GPIO.OUT)
		GPIO.setup(gGPIO, GPIO.OUT)
		GPIO.setup(bGPIO, GPIO.OUT)

		self._pwmRed = GPIO.PWM(rGPIO, 500)
		self._pwmGreen = GPIO.PWM(gGPIO, 500)
		self._pwmBlue = GPIO.PWM(bGPIO, 500)

		self._isOn = false

		self._red = 0
		self._green = 0
		self._blue = 0

	def changeColour(self, red, green, blue):
		if(red < 0 or red > 100):
			raise ValueError('Value of red should be between 0 and 100'
		if(green < 0 or green > 100):
			raise ValueError('Value of green should be between 0 and 100'
		if(blue < 0 or blue > 100)
			raise ValueError('Value of blue should be between 0 and 100'
		
		self._red = red
		self._green = green
		self._blue = blue

		if _isOn:
			_pwmRed.ChangeDutyCycle(_red)
			_pwmGreen.ChangeDutyCycle(_green)
			_pwmBlue.ChangeDutyCycle(_blue)

	def toggle(self):
		if _isOn:
			_pwmRed.stop()
			_pwmGreen.stop()
			_pwmBlue.stop()
		else:
			pwmRed.start(_red)
			pwmGreen.start(_green)
			pwmBlue.start(_blue)
