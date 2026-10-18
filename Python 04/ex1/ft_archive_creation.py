import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{args[0]}'")
        content = None
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
        if content is not None:
            print("")
            transformed = content.replace('\n', '#\n')
            if transformed != '' and not transformed.endswith('\n'):
                transformed += '#'
            print("Transform data:")
            print("---")
            print("")
            print(transformed)
            print("---")
            new_file_name = input("Enter new file name (or empty): ")
            if new_file_name:
                try:
                    print(f"Saving data to '{new_file_name}'")
                    with open(new_file_name, "w") as new_file:
                        new_file.write(transformed)
                    print(f"Data saved in file '{new_file_name}'.")
                except OSError as e:
                    print(f"Error writing to file '{new_file_name}': {e}")
            else:
                print("Not saving data.")
