# pins_lib/shield.py
from machine import Pin, PWM
import time

class Shield:
    def __init__(self, pin_red, pin_green, pin_blue, pin_buzzer):
        self.led_red = Pin(pin_red, Pin.OUT)
        self.led_green = Pin(pin_green, Pin.OUT)
        self.led_blue = Pin(pin_blue, Pin.OUT)
        self.buzzer = PWM(Pin(pin_buzzer))

    def set_led(self, color):
        colors = {
            'red': (1, 0, 0),
            'green': (0, 1, 0),
            'blue': (0, 0, 1),
            'yellow': (1, 1, 0),
            'cyan': (0, 1, 1),
            'magenta': (1, 0, 1),
            'white': (1, 1, 1),
            'off': (0, 0, 0)
        }
        if color in colors:
            self.led_red.value(colors[color][0])
            self.led_green.value(colors[color][1])
            self.led_blue.value(colors[color][2])
        else:
            raise ValueError("Color not supported")

    def play_tone(self, frequency, duration):
        self.buzzer.freq(frequency)
        self.buzzer.duty_u16(32768)  # Configura el duty cycle al 50%
        time.sleep(duration)
        self.buzzer.duty_u16(0)  # Apaga el buzzer

    def deinit(self):
        self.led_red.value(0)
        self.led_green.value(0)
        self.led_blue.value(0)
        self.buzzer.deinit()
