class WeatherStation:
    def __init__(self, location):
        self.location = location
        self.observers = set()
        self._temperature = 0

    def subscribe(self, observer):
        self.observers.add(observer)
        observer.update(self)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_tempature):
        if new_tempature == self.temperature:
            return
        self._temperature = new_tempature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

### (column break)


class TemperatureMonitor:
    def __init__(self, name):
        self.name = name

    def update(self, weather_station):
        print(f'[{self.name}] {weather_station.location} is '
              f'{weather_station.temperature} degrees')


carlisle = WeatherStation('Carlisle')
lausanne = WeatherStation('Lausanne')
carlisle.temperature = 15
lausanne.temperature = 18

smart_watch = TemperatureMonitor('smart watch')
laptop = TemperatureMonitor('laptop')

carlisle.subscribe(smart_watch)
# [smart watch] Carlisle is 15 degrees

carlisle.subscribe(laptop)
# [laptop] Carlisle is 15 degrees

lausanne.subscribe(laptop)
# [laptop] Lausanne is 18 degrees

carlisle.temperature = 12
# [smart watch] Carlisle is 12 degrees
# [laptop] Carlisle is 12 degrees

lausanne.temperature = 16
# [laptop] Lausanne is 16 degrees
