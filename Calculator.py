# основной класс, отвечает за всю логику приложения
class Calculator:
    def __init__(self, mileage=15000):
        # список авто list
        self.cars = []
        # сколько км за год
        self.mileage = mileage
    # получить стоимость топлива, например по API из внешнего сервиса
    def gas_price(self):
        # TODO: Get price from API
        return 8
    # получить стоимость эл энергии, например по API из внешнего сервиса
    def power_price(self):
        # TODO: Get price from API
        return 1.2

class Car:
    def __init__(self, name: str, price: int, fuel_economy: float, service_cost: int, insurance_cost: int):
        self.name = name
        self.price = price
        self.fuel_economy = fuel_economy # l / 100 km расход топлива
        self.service_cost = service_cost # стоимость обслуживания
        self.insurance_cost = insurance_cost # стоимость страховки
    # постоянные расходы за год
    def static_year_cost(self):
        return self.service_cost + self.insurance_cost
    # динамические расходы за год, зависят от пробега
    def dynamic_year_cost(self, mileage: int, fuel_price: float):
        return self.fuel_economy * mileage / 100 * fuel_price
    # общие расходы за год
    def year_cost(self, mileage: int, fuel_price: float):
        return self.static_year_cost() + self.dynamic_year_cost(mileage, fuel_price)

class ElectricCar(Car):
    # fuel_economy и service_cost убираем из init и super, тк в этом классе он не используется
    # но в init добавил power_consumption, новый атрибут дочернего класса
    def __init__(self, name: str, price: int, insurance_cost: int, power_consumption: int):
        super().__init__(name=name, price=price, fuel_economy=0, service_cost=0, insurance_cost=insurance_cost)
        self.power_consumption = power_consumption # Wt / 1 km расход эл энергии
    # полностью переписываем родительский метод
    def dynamic_year_cost(self, mileage: int, kilowatt_price: float):
        return self.power_consumption * mileage / 1000 * kilowatt_price
