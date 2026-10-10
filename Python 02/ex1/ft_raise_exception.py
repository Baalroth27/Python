def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    for reading in ["25", "abc", "100", "-50"]:
        print(f"Input data is '{reading}'")
        try:
            print(f"Temperature is now {input_temperature(reading)}°C")
        except ValueError as e:
            print("Caught input_temperature error:", e)
        print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature()
