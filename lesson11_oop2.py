class Car:

    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def get_description(self):
        return f"{self._brand} {self._model} ({self._year})"

    def start_engine(self):
        return "Двигатель запущен"

    def change_year(self, new_year):
        self._year = new_year


class ElectroCar(Car):

    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self._battery_capacity = battery_capacity

    def start_engine(self):
        return "Электродвигатель запущен"

    @property
    def get_battery_info(self):
        return f"Емкость батареи: {self._battery_capacity} кВтч"


car = Car(brand="BMW", model="740li", year="2010")
car.change_year("2024")
print(car.get_description)
print(car.start_engine())
electro_car = ElectroCar(brand="BMW", model="Li-eco", year="2020", battery_capacity="500")
electro_car.change_year("2014")
print(electro_car.get_description)
print(electro_car.start_engine())
print(electro_car.get_battery_info)
