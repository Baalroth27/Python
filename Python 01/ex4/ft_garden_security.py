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

    def age(self):
        self.set_age((self.get_age() + 1))

    def __str__(self):
        return (f'{self._name}: {round(self.get_height(), 1):.1f}cm, '
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


if __name__ == "__main__":
    p = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print(f'Plant created: {p}')
    if p.set_height(25):
        print(f'Height updated: {p.get_height()}cm')
    else:
        print("Height update rejected")
    if p.set_age(30):
        print(f'Age updated: {p.get_age()} days')
    else:
        print("Age update rejected")
    if p.set_height(-1):
        print(f'Height updated: {p.get_height()}cm')
    else:
        print("Height update rejected")
    if p.set_age(-1):
        print(f'Age updated: {p.get_age()} days')
    else:
        print("Age update rejected")
    print(f'Current state: {p}')
