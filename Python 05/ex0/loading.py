import importlib.util

REAGENTS: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
}


def main() -> None:
    all_present = True
    print('')
    print("REAGENT STATUS: Loading reagents...")
    print('')
    print("Checking dependencies:")
    for name, description in REAGENTS.items():
        if importlib.util.find_spec(name) is None:
            print(f"[ERROR] {name} - {description} is missing")
            all_present = False
        else:
            try:
                mod = importlib.import_module(name)
            except ImportError as e:
                print(f"[ERROR] Failed to import {name}: {e}")
                all_present = False
            else:
                print(f"[OK] {name} ({mod.__version__}) - "
                      f"{description} ready")
    print('')
    print("pip vs Poetry:")
    print("  requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")
    print('')
    if all_present:
        print("All reagents present and accounted for.")
    else:
        print("Make sure that all the reagents are present by running these, "
              "while in the ex0 folder:")
        print("=== For pip")
        print("pip install -r requirements.txt")
        print("python3 loading.py")
        print("=== For Poetry")
        print("poetry install")
        print("poetry run python loading.py")


if __name__ == "__main__":
    main()
