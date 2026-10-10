class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.plant_age = age
        self.height = height
        self.growth_rate = growth

    def show(self):
        print(f'{self.name}: {round(self.height, 1)}cm, '
              f'{self.plant_age} days old')

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.plant_age += 1


if __name__ == "__main__":
    p = Plant("Rose", 25.0, 30, 0.8)
    height_start = p.height
    print("=== Garden Plant Growth ===")
    p.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p.grow()
        p.age()
        p.show()
    print(f'Growth this week: {round((p.height - height_start), 1)}')
