class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(f'{self.name}: {self.height}cm, {self.age} days old')


if __name__ == "__main__":
    garden = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    print('=== Garden Plant Registry ===')
    for plant in garden:
        plant.show()
