class Plant:
    def __init__(self, name, height, age, growth=0.1):
        self.name = name
        self.plant_age = age
        self.height = height
        self.growth_rate = growth

    def show(self):
        print(self)

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.plant_age += 1

    def __str__(self):
        return (f'{self.name}: {round(self.height, 1)}cm, '
                f'{self.plant_age} days old')


if __name__ == "__main__":
    garden = [Plant("Rose", 25.0, 30), Plant("Oak", 200.0, 365),
              Plant("Cactus", 5.0, 90), Plant("Sunflower", 80.0, 45),
              Plant("Fern", 15.0, 120)]
    print("=== Plant Factory Output ===")
    for plant in garden:
        print(f'Created: {plant}')
