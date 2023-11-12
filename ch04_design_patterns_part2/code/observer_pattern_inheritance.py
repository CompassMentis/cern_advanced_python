import abc

class SubjectBaseClass:
    def __init__(self):
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)
        observer.update(self)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class ObserverBaseClass(abc.ABC):
    @abc.abstractmethod
    def update(self, subject):
        ...

### (column break)

class WeatherStation(SubjectBaseClass):
    def __init__(self, location):
        super().__init__()
        self.location = location
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_tempature):
        if new_tempature == self.temperature:
            return
        self._temperature = new_tempature
        self.notify_observers()


class TemperatureMonitor(ObserverBaseClass):
    def __init__(self, name):
        self.name = name

    def update(self, weather_station):
        print(f'[{self.name}] {weather_station.location} is '
              f'{weather_station.temperature} degrees')

### (column break)

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
