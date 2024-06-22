import math
import random
import threading
import time

from .history import wind_degrees_to_cardinal

__version__ = '0.0.1'


# Wind Vane
PIN_WV = 8     # P0.3 ANE6

# Anemometer
PIN_ANE1 = 5       # P0.0
PIN_ANE2 = 6       # P0.1

ANE_RADIUS = 7  # Radius from center to the center of a cup, in CM
ANE_CIRCUMFERENCE = ANE_RADIUS * 2 * math.pi
ANE_FACTOR = 2.18  # Anemometer factor

# Rain gauge
PIN_R2 = 3         # P1.2
PIN_R3 = 7         # P1.1
PIN_R4 = 2         # P1.0
PIN_R5 = 1         # P1.5
RAIN_MM_PER_TICK = 0.2794

wind_direction_to_degrees = {
    0.9: 0,
    2.0: 45,
    3.0: 90,
    2.8: 135,
    2.5: 180,
    1.5: 225,
    0.3: 270,
    0.6: 315
}


class WeatherHAT:
    def __init__(self):
        self._lock = threading.Lock()

        # Data API... kinda
        self.temperature_offset = -7.5
        self.device_temperature = 0
        self.temperature = 0

        self.pressure = 0

        self.humidity = 0
        self.relative_humidity = 0
        self.dewpoint = 0

        self.lux = 0

        self.wind_speed = 0
        self.wind_direction = 0

        self.rain = 0
        self.rain_total = 0

        self._rain_counts = 0
        self._wind_counts = 0

        self.updated_wind_rain = False

        self.reset_counts()

    def reset_counts(self):
        self._t_start = time.time()

    def compensate_humidity(self, humidity, temperature, corrected_temperature):
        """Compensate humidity.

        Convert humidity to relative humidity.

        """
        dewpoint = self.get_dewpoint(humidity, temperature)
        corrected_humidity = 100 - (5 * (corrected_temperature - dewpoint)) - 20
        return min(100, max(0, corrected_humidity))

    def get_dewpoint(self, humidity, temperature):
        """Calculate Dewpoint."""
        return temperature - ((100 - humidity) / 5)

    def hpa_to_inches(self, hpa):
        """Convert hextopascals to inches of mercury."""
        return hpa * 0.02953

    def degrees_to_cardinal(self, degrees):
        value, cardinal = min(wind_degrees_to_cardinal.items(), key=lambda item: abs(item[0] - degrees))
        return cardinal

    def update(self, interval=60.0):
        # Time elapsed since last update
        delta = time.time() - self._t_start
        self.updated_wind_rain = False

        # Always update TPHL & Wind Direction
        self._lock.acquire(blocking=True)

        # TODO make history depth configurable
        # TODO make update interval for sensors fixed so history always represents a known period

        self.device_temperature = 10.0 + math.sin(time.time() / 10.0) * 20.0
        self.temperature = self.device_temperature + self.temperature_offset

        self.pressure = 1050.0 + math.sin(time.time() / 10.0) * 50.0
        self.humidity = 50 + math.sin(time.time() / 10.0) * 25.0

        self.relative_humidity = self.compensate_humidity(self.humidity, self.device_temperature, self.temperature)

        self.dewpoint = self.get_dewpoint(self.humidity, self.device_temperature)

        self.lux = 500.0 + math.sin(time.time()) * 250.0

        self.wind_direction_raw = random.randint(0, 33) / 10.0

        self._lock.release()

        value, self.wind_direction = min(wind_direction_to_degrees.items(), key=lambda item: abs(item[0] - self.wind_direction_raw))

        # Don't update rain/wind da`ta until we've sampled for long enough
        if delta < interval:
            return

        self.updated_wind_rain = True

        wind_counts = 2 + math.sin(time.time()) * 1
        rain_counts = 5 + math.sin(time.time()) * 5

        rain_hz = rain_counts / delta
        wind_hz = wind_counts / delta
        self.rain_total = rain_counts * RAIN_MM_PER_TICK
        self.reset_counts()

        # print(delta, rain_hz, wind_hz)

        # wind speed of 2.4km/h causes the switch to close once per second

        wind_hz /= 2.0  # Two pulses per rotation
        wind_cms = wind_hz * ANE_CIRCUMFERENCE * ANE_FACTOR
        self.wind_speed = wind_cms / 100.0

        self.rain = rain_hz * RAIN_MM_PER_TICK
