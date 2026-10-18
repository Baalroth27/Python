import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{args[0]}'")
        try:
            f = open(args[0], "r")
            try:
                content = f.read()
                print("---")
                print("")
                print(content)
                print("---")
            except UnicodeDecodeError as e:
                print(f"Error reading file '{args[0]}': {e}")
            finally:
                f.close()
                print(f"File '{args[0]}' closed.")
        except OSError as e:
            print(f"Error opening file '{args[0]}': {e}")
