class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error") -> None:
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants = ["Tomato", "lettuce", "Carrots"]
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as e:
        print("Caught PlantError:", e)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("")
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as e:
        print("Caught PlantError:", e)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("")
    test_watering_system()
    print("")
    print("Cleanup always happens, even with errors!")
