class GardenError(Exception):
    def __init__(self, msg: str = "Unknown garden error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown plant error") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown water error") -> None:
        super().__init__(msg)


def exception_thrower(exception: int) -> None:
    if exception == 1:
        raise PlantError("The tomato plant is wilting!")
    if exception == 2:
        raise WaterError("Not enough water in the tank!")


def exception_tester() -> None:
    print("Testing PlantError...")
    try:
        exception_thrower(1)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}:", e)
    print("")
    print("Testing WaterError...")
    try:
        exception_thrower(2)
    except (WaterError) as e:
        print(f"Caught {e.__class__.__name__}:", e)
    print("")
    print("Testing catching all garden errors...")
    for i in range(1, 3):
        try:
            exception_thrower(i)
        except (GardenError) as e:
            print("Caught GardenError:", e)
    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("")
    exception_tester()
