class Plant:
    def __init__(self, name, height, age, growth=0.1):
        self._name = name
        self._plant_age = 0
        self._height = 0
        self._growth_rate = 0.1
        self.set_age(age)
        self.set_height(height)
        if growth > 0:
            self._growth_rate = growth

    def show(self):
        print(self)

    def grow(self):
        self.set_height((self.get_height() + self._growth_rate))

    def age(self, days):
        self.set_age((self.get_age() + days))

    def __str__(self):
        return (f'{self._name}: {self.get_height():.1f}cm, '
                f'{self.get_age()} days old')

    def set_height(self, height):
        if height >= 0:
            self._height = height
            return True
        else:
            print(f"{self._name}: Error, height can't be negative")
            return False

    def set_age(self, age):
        if age >= 0:
            self._plant_age = age
            return True
        else:
            print(f"{self._name}: Error, age can't be negative")
            return False

    def get_height(self):
        return self._height

    def get_age(self):
        return self._plant_age


class Flower(Plant):
    def __init__(self, name, height, age, color, growth=0.1):
        super().__init__(name, height, age, growth=growth)
        self._color = color
        self.blooming = False

    def __str__(self):
        status = ('is blooming beautifully!' if self.blooming
                  else 'has not bloomed yet')
        return (super().__str__() + f'\n Color: {self._color}'
                f'\n {self._name} {status}')

    def bloom(self):
        self.blooming = True


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, growth=0.1):
        super().__init__(name, height, age, growth=growth)
        self._trunk_diameter = trunk_diameter

    def __str__(self):
        return (super().__str__() +
                f'\n Trunk diameter: {self._trunk_diameter:.1f}cm')

    def produce_shade(self):
        print(f'Tree {self._name} now produces a shade of '
              f'{self.get_height():.1f}cm long and '
              f'{self._trunk_diameter:.1f}cm wide.')


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value,
                 growth=0.1):
        super().__init__(name, height, age, growth=growth)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def __str__(self):
        return (super().__str__() +
                f'\n Harvest season: {self._harvest_season}'
                f'\n Nutritional value: {self._nutritional_value}')

    def age(self, days):
        super().age()
        self._nutritional_value += days


if __name__ == "__main__":
    f = Flower("Rose", 15, 10, "red")
    t = Tree("Oak", 200, 365, 5)
    v = Vegetable("Tomato", 5, 10, "April", 0, 2.1)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    f.show()
    f.bloom()
    print("[asking the rose to bloom]")
    f.show()
    print("")
    print("=== Tree")
    t.show()
    t.produce_shade()
    print("[asking the oak to produce shade]")
    print("")
    print("=== Vegetable")
    v.show()
    for i in range(0, 20):
        v.grow()
    v.age(20)
    print("[making tomato grow and age for 20 days]")
    v.show()
