import sys
import site
import os


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    print('')
    virtual = in_venv()
    if virtual:
        print("LABORATORY STATUS: The laboratory is sealed")
    else:
        print("LABORATORY STATUS: You are working in the open")
    print('')
    print(f"Current Python: {sys.executable}")
    if virtual:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print('')
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print('')
        print("Reagent installation path:")
        print(site.getsitepackages()[0])
    else:
        print("Virtual Environment: None detected")
        print('')
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print('')
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print('')
        print("Then run this program again.")
        print('')
        print("Reagent installation path:")
        print(site.getusersitepackages())


if __name__ == "__main__":
    main()
