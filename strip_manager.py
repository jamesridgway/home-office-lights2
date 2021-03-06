import time

from rpi_ws281x import Adafruit_NeoPixel, Color


class StripManager:

    @staticmethod
    def default():
        led_count = 159  # Number of LED pixels.
        led_pin = 18  # GPIO pin connected to the pixels (18 uses PWM!).
        led_freq_hz = 800000  # LED signal frequency in hertz (usually 800khz)
        led_dma = 10  # DMA channel to use for generating signal (try 10)
        led_brightness = 255  # Set to 0 for darkest and 255 for brightest
        led_invert = False  # True to invert the signal (when using NPN transistor level shift)
        led_channel = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
        return StripManager(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness, led_channel)

    def __init__(self, led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness, led_channel):
        self.strip = Adafruit_NeoPixel(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness,
                                       led_channel)
        self.strip.begin()
        self.on = False

    def solid_color(self, r, g, b, brightness=255):
        self.strip.setBrightness(brightness)
        for i in range(0, self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(r, g, b))
            self.strip.show()
        self.on = True

    def alert(self, r, g, b, wait_ms=50, iterations=10):
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, Color(r, g, b))
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)
        self.on = True

    def clear(self):
        self.solid_color(0, 0, 0)
        self.on = False

    def orange(self):
        self.solid_color(255, 64, 0)

    def status(self):
        return {
            'on': self.on
        }
