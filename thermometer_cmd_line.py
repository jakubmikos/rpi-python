# 04_thermomether.py

import RPi.GPIO as GPIO
import time, math
from RgbLedGPIO import RgbLed

GPIO.setmode(GPIO.BCM)

a_pin = 25
b_pin = 8

fiddle_factor = 0.9;

def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

def analog_read():
    discharge()
    return charge_time()

def read_resistance():
    n = 100
    total = 0;
    for i in range(1, n):
        total = total + analog_read()
    reading = total / float(n)
    resistance = reading * 6.05 - 939
    return resistance

def temp_from_r(R):
    B = 3800.0
    R0 = 1000.0
    t0 = 273.15
    t25 = t0 + 25.0
    inv_T = 1/t25 + 1/B * math.log(R/R0)
    T = 1/inv_T - t0
    return T * fiddle_factor
try:
    led = RgbLed(18, 23, 24)
    led.changeColour(0,100,0)
    led.toggle()
    while True:
        temp_c = temp_from_r(read_resistance())
        if temp_c > 25:
            led.changeColour(100,0,0)
	else:
            led.changeColour(0,100,0)
        print "{:.2f}".format(temp_c)
except KeyboardInterrupt:
    print 'end'
finally:
    GPIO.cleanup()
