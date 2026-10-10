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
        self.stats = self.Stats()

    def show(self):
        self.stats.increment_show()
        print(self)

    def grow(self):
        self.stats.increment_grow()
        self.set_height((self.get_height() + self._growth_rate))

    def age(self, days):
        self.stats.increment_age()
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

    @staticmethod
    def check_age(age):
        if age > 365:
            return True
        else:
            return False

    @classmethod
    def anon_plant(cls):
        return cls("Unknown plant", 0, 0, 0)

    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow(self):
            self._grow_calls += 1

        def increment_age(self):
            self._age_calls += 1

        def increment_show(self):
            self._show_calls += 1

        def __str__(self):
            return (f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                    f"{self._show_calls} show")


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
        self.stats.increment_shade()
        print(f'Tree {self._name} now produces a shade of '
              f'{self.get_height():.1f}cm long and '
              f'{self._trunk_diameter:.1f}cm wide.')

    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def __str__(self):
            return (super().__str__() + f'\n {self._shade_calls} shade')

        def increment_shade(self):
            self._shade_calls += 1


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

    def age(self):
        super().age()
        self._nutritional_value += 1


class Seed(Flower):
    def __init__(self, name, height, age, color, seeds, growth=0.1):
        super().__init__(name, height, age, color, growth=growth)
        self._seeds = seeds

    def __str__(self):
        status = (f'{self._seeds}' if self.blooming else '0')
        return (super().__str__() + f'\n Seeds: {status}')


def display_stats(plant):
    print(plant.stats)


if __name__ == "__main__":
    f = Flower("Rose", 15, 10, "red", 8)
    t = Tree("Oak", 200, 365, 5)
    s = Seed("Sunflower", 80, 45, "yellow", 42, 30)
    a = Plant.anon_plant()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {a.check_age(30)}")
    print(f"Is 400 days more than a year? -> {a.check_age(400)}")
    print("")
    print("=== Flower")
    f.show()
    print("[statistics for Rose]")
    display_stats(f)
    print("[asking the rose to grow and bloom]")
    f.grow()
    f.bloom()
    f.show()
    print("[statistics for Rose]")
    display_stats(f)
    print("")
    print("=== Tree")
    t.show()
    print("[statistics for Oak]")
    display_stats(t)
    print("[asking the oak to produce shade]")
    t.produce_shade()
    print("[statistics for Oak]")
    display_stats(t)
    print("")
    print("=== Seed")
    s.show()
    print("[make sunflower grow, age and bloom]")
    s.grow()
    s.age(20)
    s.bloom()
    s.show()
    print("[statistics for Sunflower]")
    display_stats(s)
    print("")
    print("=== Anonymous")
    a.show()
    print("[statistics for Unknown plant]")
    display_stats(a)
